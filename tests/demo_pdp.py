# remove these two lines in production
import sys
sys.path.append("..")

import pandas_prompt as pdp

# Configure API/local model
pdp.prompt.configure(api_key="voc-173692058315987414691616837a5b304df04.71379980", model="gpt-4", api_base = "https://openai.vocareum.com/v1")

# Load CSV with standard pandas functionality
df = pdp.read_csv("testsales.csv")

# Run a prompt
print(df.prompt("Show me the top 5 rows according to the Total Profit"))


# Plot from prompt
#df.prompt.plot("histogram of item type versus Total profits")

# Follow-up query
#print(df.prompt.follow("Now sort by revenue"))
