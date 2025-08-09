import pandas_prompt as pdp

# Configure API/local model
pdp.prompt.configure(api_key="fake-key", model="gpt-4")

# Load CSV with standard pandas functionality
df = pdp.read_csv("testsales.csv")

# Run a prompt
print(df.prompt("Show me the top 5 rows"))

# Plot from prompt
df.prompt.plot("histogram of sales")

# Follow-up query
print(df.prompt.follow("Now sort by revenue"))
