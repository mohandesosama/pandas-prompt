# pandas_prompt/interface/patch.py

def patch_dataframe():
    import pandas as pd
    from pandas_prompt.interface.dataframe_prompt import prompt_dataframe, prompt_plot

    pd.DataFrame.prompt = prompt_dataframe
    pd.DataFrame.prompt_plot = prompt_plot
