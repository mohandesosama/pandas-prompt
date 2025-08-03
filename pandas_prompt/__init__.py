# Re-export all of pandas' public API
from pandas import *  # noqa: F403
import pandas as pd
from .prompt import prompt_dataframe

# Patch .prompt() onto DataFrame
pd.DataFrame.prompt = prompt_dataframe
