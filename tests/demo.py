# to make this code works locally, do the following 
# pip install -e .

import sys
import os
import pandas as pd

# Ensure the top-level project directory is in the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from engine.openai_engine import OpenAIPromptEngine
#from engine.local_engine import LocalLLMPromptEngine
from interface.handler import PromptHandler

def test_openai_prompt():
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie"],
        "salary": [1000, 2000, 3000]
    })

    handler = PromptHandler(OpenAIPromptEngine())
    result = handler.run_prompt(df, "Show me the average salary")
    print("[TEST-OpenAI] Output:", result)
'''
def test_local_prompt():
    df = pd.DataFrame({
        "department": ["HR", "Engineering", "Marketing"],
        "employees": [5, 12, 8]
    })

    # Ensure the model file exists or use mock for now
    model_path = "models/llama-model.gguf"
    if not os.path.exists(model_path):
        print("[TEST-Local] Skipped: LLaMA model file not found at", model_path)
        return

    handler = PromptHandler(LocalLLMPromptEngine(model_path=model_path))
    result = handler.run_prompt(df, "Show departments with more than 6 employees")
    print("[TEST-Local] Output:", result)

    '''

if __name__ == "__main__":
    print(">>> Running OpenAI test...")
    test_openai_prompt()

    #print("\n>>> Running Local LLM test...")
    #test_local_prompt()
