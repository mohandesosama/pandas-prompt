# pandas_prompt/__init__.py

import pandas as _pd
from pandas_prompt.interface.patch import patch_dataframe

# Apply the patch to add .prompt and .prompt_plot
patch_dataframe()

# Export all of pandas API
from pandas import *

# Optionally expose the original pandas under a private alias
_pd_orig = _pd
