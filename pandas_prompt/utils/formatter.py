def build_prompt(df, instruction):
    df_sample = df.head(10).to_csv(index=False)
    return (
        f"You are a pandas expert. Given this DataFrame:\n{df_sample}\n"
        f"Instruction: {instruction}\n"
        f"Write Python code using variable 'df'."
    )

def build_plot_prompt(df, instruction):
    df_sample = df.head(10).to_csv(index=False)
    return (
        f"You are a pandas and matplotlib expert. Given this DataFrame:\n{df_sample}\n"
        f"Instruction: {instruction}\n"
        f"Write Python code using variable 'df' that produces the plot."
    )
