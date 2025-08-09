from .prompt_manager import PromptManager
from .core_implementation.plotting import plot_data
from .core_implementation.follow import follow_conversation

class PromptAccessor:
    _config = {}

    @classmethod
    def configure(cls, **kwargs):
        """
        Configure API keys, local model paths, or settings.
        Example:
            pdp.prompt.configure(api_key="YOUR_KEY", model="gpt-4")
        """
        cls._config.update(kwargs)

    def __init__(self, df):
        self.df = df
        self.manager = PromptManager(config=self._config)

    def __call__(self, query: str):
        """
        Run a natural language query against the DataFrame.
        Example:
            df.prompt("Show me the top 5 rows with highest salary")
        """
        return self.manager.run_query(self.df, query)

    def plot(self, query: str):
        """
        Generate a plot based on a natural language request.
        Example:
            df.prompt.plot("Plot salary distribution by department")
        """
        return plot_data(self.df, query)

    def follow(self, query: str):
        """
        Continue a conversation based on previous context.
        Example:
            df.prompt.follow("Now group by department")
        """
        return follow_conversation(self.df, query)
