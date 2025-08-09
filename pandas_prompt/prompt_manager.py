from .ai_interface import AIInterface

class PromptManager:
    def __init__(self, config):
        self.config = config
        self.ai = AIInterface(config)

    def run_query(self, df, query: str):
        """
        Convert a natural language query to pandas code and execute it.
        """
        code = self.ai.generate_code(df, query)
        try:
            result = eval(code, {"df": df})
            return result
        except Exception as e:
            return f"Error executing generated code:\n{e}\nGenerated code:\n{code}"
