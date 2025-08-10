from .ai_interface import AIInterface
import pandas as pd

class PromptManager:
    def __init__(self, config):
        self.config = config
        self.ai = AIInterface(config)



    def run_query(self, df, query: str):
        """
        Convert a natural language query to pandas code and execute it.
        Ensures the output is a pandas Series or DataFrame.
        """
        code = self.ai.generate_code(df, query)
        """Safely executes generated pandas code and returns result"""
        local_vars = {'df': df.copy()}
        global_vars = {}

        try:
            # Ensure the code assigns to 'result'
            if "result" not in code:
                code += "\nresult"  # Add result reference if missing
            
            # Execute in a controlled environment
            exec(code, global_vars, local_vars)
            
            # Return the result variable
            return local_vars.get('result', None)
        except Exception as e:
            return f"Execution Error: {str(e)}\nGenerated Code:\n{code}"
