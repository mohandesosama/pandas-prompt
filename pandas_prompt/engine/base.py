from abc import ABC, abstractmethod
import pandas as pd

class BasePromptEngine(ABC):
    @abstractmethod
    def run(self, df: pd.DataFrame, prompt: str) -> str:
        pass