import pandas as pd
from openai import OpenAI
import json
from typing import Dict, Any
import matplotlib.pyplot as plt

class Agent:
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

    def build_prompt(self, df: pd.DataFrame, query: str) -> str:
        """
        Each agent must override this to create a specific prompt.
        """
        raise NotImplementedError("Agents must implement build_prompt()")

    def execute(self, code: str, df: pd.DataFrame):
        """
        Each agent must override this to execute generated code.
        """
        raise NotImplementedError("Agents must implement execute()")

    def generate_code(self, df: pd.DataFrame, query: str) -> str:
        """Send schema + query to LLM to generate Python code."""
        schema_str = json.dumps(self._get_schema(df), indent=2)
        prompt = self.build_prompt(df, query)

        if not self.client:
            # Fallback: local stub for development
            print("you are in stub mode, no API calls")
            return "df.head()"

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": f"Schema:\n{schema_str}\n{prompt}"}],
                temperature=0
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
            return f"# ERROR: {e}"
        

class AnalysisAgent(Agent):
    def build_prompt(self, df: pd.DataFrame, query: str) -> str:
        
        schema_str = self._get_schema(df)
        
        prompt = f"""You are an expert Python data analyst. Generate Pandas code that:
            1. Uses ONLY the provided DataFrame 'df'
            2. Returns a DataFrame/Series (no prints/plots)
            3. Preserves the original df
            4. Is production-ready code
            5. Assign the final result to a variable named `result`
            6. The last line must be `result`
            7. Don't explain anything, just give the python code

            Schema:
            {schema_str}

            Query: {query}

            Return ONLY the python code wrapped in ```python ```:"""
        return prompt

    def execute(self, code: str, df: pd.DataFrame):
        """Safely executes generated pandas code and returns result"""
        local_vars = {"df": df, "pd": pd}
        try:
            exec(code, {}, local_vars)
            # If the code defines a variable 'result', return it
            if "result" in local_vars:
                return local_vars["result"]
            else:
                # Try returning the last defined DataFrame/Series
                for val in reversed(local_vars.values()):
                    if isinstance(val, (pd.DataFrame, pd.Series)):
                        return val
                return None
        except Exception as e:
            print(f"Error executing analysis code:\n{e}\nGenerated code:\n{code}, the function didn't change the original df")
            return local_vars["df"]

class PlottingAgent(Agent):
    def build_prompt(self, df: pd.DataFrame, query: str) -> str:
        return f"""
        You are a Pandas/Matplotlib plotting assistant.
        Task: Generate Python code to plot data from `df` based on: "{query}"
        Rules:
        - Must use either matplotlib or pandas built-in plotting.
        - Code must end with `plt.show()`.
        - Do not import anything.
        - Use only `df`, `pd`, and `plt`.
        """

    def execute(self, code: str, df: pd.DataFrame):
        try:
            exec(code, {"df": df, "pd": pd, "plt": plt})
        except Exception as e:
            print(f"Error executing plot code:\n{e}\nGenerated code:\n{code}")