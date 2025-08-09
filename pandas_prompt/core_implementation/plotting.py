import matplotlib.pyplot as plt

def plot_data(df, query: str):
    """
    Interpret query and plot the data accordingly.
    TODO: Integrate AI parsing for advanced plots.
    """
    # Simple example: if 'histogram' in query.lower(), plot a histogram
    if "histogram" in query.lower():
        df.hist()
        plt.show()
    else:
        plt.plot(df.index, df[df.columns[0]])
        plt.show()
