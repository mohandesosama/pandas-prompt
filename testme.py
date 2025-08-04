# test.py
from pandas_prompt.prompt import PromptEngine, prompt_dataframe
import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "salary": [1200, 950, 1300]
})

df.__class__.prompt = prompt_dataframe  # Attach dynamically
print(df.prompt("Show me the highest salary"))
