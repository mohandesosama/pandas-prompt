import sys
import os

# Add the parent directory of the project to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def prompt_dataframe(self, instruction: str, handler=None):
    from engine.openai_engine import OpenAIPromptEngine
    from interface.handler import PromptHandler

    handler = handler or PromptHandler(OpenAIPromptEngine())
    return handler.run_prompt(self, instruction)


def prompt_plot(self, instruction: str, handler=None):
    from engine.openai_engine import OpenAIPromptEngine
    from interface.handler import PromptHandler

    handler = handler or PromptHandler(OpenAIPromptEngine())
    return handler.run_plot(self, instruction)
