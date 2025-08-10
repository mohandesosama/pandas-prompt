import pandas as pd
from .core import PromptAccessor

# Attach prompt accessor to DataFrame
#pd.DataFrame.prompt = PromptAccessor
pd.api.extensions.register_dataframe_accessor("prompt")(PromptAccessor)

# Re-export pandas for full compatibility
from pandas import *  # noqa

# Also allow direct usage like pdp.prompt.configure(...)
prompt = PromptAccessor

__all__ = [
    *pd.__all__,
    "prompt"
]

