'''

import pandas as pd
from .base import BasePromptEngine
from llama_cpp import Llama
import os

class LocalLLMPromptEngine(BasePromptEngine):
    def __init__(self, model_path: str = "models/llama-model.gguf"):
        self.model = Llama(model_path=model_path)

    def run(self, df: pd.DataFrame, prompt: str) -> str:
        df_sample = df.head(10).to_csv(index=False)
        full_prompt = (
            f"You are a pandas expert. Given this DataFrame:\n{df_sample}\n"
            f"Instruction: {prompt}\n"
            f"Write Python code using variable 'df' to perform this task."
        )

        result = self.model(full_prompt, max_tokens=512, stop=["\n\n"])
        return result["choices"][0]["text"].strip()

        '''