import os
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
from .base import BasePromptEngine

class OpenAIPromptEngine(BasePromptEngine):
    def __init__(self, model="gpt-3.5-turbo", api_key_env="OPENAI_API_KEY"):
        load_dotenv()
        self.client = OpenAI(
            base_url="https://openai.vocareum.com/v1",
            api_key=os.getenv(api_key_env)
        )
        self.model = model

    def run(self, df: pd.DataFrame, instruction: str) -> str:
        df_sample = df.head(10).to_csv(index=False)
        prompt = (
            f"You are a pandas expert. Given this DataFrame:\n{df_sample}\n"
            f"Instruction: {instruction}\n\n"
            f"Write Python code using variable 'df' to perform this task."
        )

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
        )
        return response.choices[0].message.content.strip("```python\n").strip("```")
