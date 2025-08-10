import pandas as pd
from openai import OpenAI
import json
from typing import Dict, Any

class AIInterface:
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize AI interface with configuration.
        
        Config options:
        - api_key: str - Your API key
        - model: str - Model name (default: "gpt-4")
        - api_base: str - Custom API endpoint URL
        - local_model_path: str - Path to local model (alternative to API)
        """
        self.config = config
        self.model = config.get("model", "gpt-4")
        self.api_key = config.get("api_key")
        self.api_base = config.get("api_base")  # Custom API base URL
        self.local_model_path = config.get("local_model_path")
        
        # Initialize OpenAI client with custom config
        self.client = None
        if self.api_key:
            client_config = {"api_key": self.api_key}
            if self.api_base:
                client_config["base_url"] = self.api_base  # Use custom endpoint
            self.client = OpenAI(**client_config)

    def _get_schema(self, df: pd.DataFrame) -> str:
        """Extracts comprehensive schema information from DataFrame."""
        schema = {
            "columns": list(df.columns),
            "dtypes": {col: str(dtype) for col, dtype in df.dtypes.items()},
            "shape": df.shape,
            "memory_usage": df.memory_usage(deep=True).to_dict(),
            "sample": df.head(3).to_dict(orient="records")
        }
        return json.dumps(schema, indent=2)

    def generate_code(self, df: pd.DataFrame, query: str) -> str:
        """
        Generates pandas code from natural language query.
        Returns executable Python code or error message.
        """
        schema_str = self._get_schema(df)
        
        prompt = f"""You are an expert Python data analyst. Generate Pandas code that:
            1. Uses ONLY the provided DataFrame 'df'
            2. Returns a DataFrame/Series (no prints/plots)
            3. Preserves the original df
            4. Is production-ready code
            5. Assign the final result to a variable named `result`
            6. The last line must be `result`

            Schema:
            {schema_str}

            Query: {query}

            Return ONLY the python code wrapped in ```python ```:"""

        try:
            if not self.client:
                return "# ERROR: API client not configured"
                
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
                max_tokens=1000
            )
            
            raw_response = response.choices[0].message.content.strip()
            
            # Robust code extraction
            if "```python" in raw_response:
                code = raw_response.split("```python")[1].split("```")[0].strip()
                # Validate code contains df reference
                if "df" in code:
                    return code
            return raw_response or "# ERROR: Empty response from API"
            
        except Exception as e:
            return f"# ERROR: {str(e)}"