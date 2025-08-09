class AIInterface:
    def __init__(self, config):
        self.config = config
        self.model = config.get("model", "gpt-4")
        self.api_key = config.get("api_key", None)
        self.local_model_path = config.get("local_model_path", None)

    def generate_code(self, df, query: str) -> str:
        """
        In a real system, send the schema & query to an LLM to generate pandas code.
        Here, we simulate with a placeholder.
        """
        # TODO: Implement OpenAI / local model call
        return "df.head()"  # Placeholder
