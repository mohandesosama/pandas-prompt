import pandas as pd
from utils.formatter import build_prompt, build_plot_prompt

class PromptHandler:
    def __init__(self, engine):
        self.engine = engine

    def run_prompt(self, df: pd.DataFrame, instruction: str):
        prompt = build_prompt(df, instruction)
        code = self.engine.run(df, prompt)
        print("[Prompt] Executing generated code:\n", code)
        local_vars = {"df": df}
        try:
            exec(code, {}, local_vars)
            return local_vars.get("result", None)
        except Exception as e:
            print("Execution error:", e)
            return None

    def run_plot(self, df: pd.DataFrame, instruction: str):
        prompt = build_plot_prompt(df, instruction)
        code = self.engine.run(df, prompt)
        print("[PromptPlot] Executing generated plot code:\n", code)
        local_vars = {"df": df}
        try:
            exec(code, {}, local_vars)
        except Exception as e:
            print("Plot execution error:", e)
