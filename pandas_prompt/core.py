from .agents import AnalysisAgent, PlottingAgent

class PromptAccessor:
    _config = {}

    @classmethod
    def configure(cls, **kwargs):
        # cls is refering to the class itself. self is refering to an object of the class
        # you can call this class immediately such as PromptAccessor.configure()
        """
        Configure API keys, local model paths, or settings.
        Example:
            pdp.prompt.configure(api_key="YOUR_KEY", model="gpt-4")
        """
        cls._config.update(kwargs)

    def __init__(self, df):
        self.df = df
        self.analysis_agent = AnalysisAgent(config=self._config)
        self.plotting_agent = PlottingAgent(config=self._config)

    def __call__(self, query: str):
        """
        Run a natural language query against the DataFrame.
        Example:
            df.prompt("Show me the top 5 rows with highest salary")
        """
        code = self.analysis_agent.generate_code(self.df, query)
        #print("Generated Analysis Code:\n", code)
        return self.analysis_agent.execute(code, self.df)

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
