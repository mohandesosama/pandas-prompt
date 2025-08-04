import sys
import os

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas_prompt as pdp

# Optional: Force use of llama or openai engine
# from pandas_prompt.interface.handler import PromptHandler
# from pandas_prompt.engine.llama_engine import LlamaPromptEngine
# handler = PromptHandler(LlamaPromptEngine())

def test_prompt_basic():
    df = pdp.read_csv("testsales.csv")
    result = df.prompt("Show me the highest profit")
    print("Test passed result=", result)

if __name__ == "__main__":
    test_prompt_basic()
