import sys
sys.path.append("..")

import os
from dotenv import load_dotenv  # Import dotenv loader
import pandas_prompt as pdp

# Load environment variables from .env file
load_dotenv()  # Loads from current directory or specify path: load_dotenv(".env")

# Configure API using environment variables
pdp.prompt.configure(
    api_key=os.getenv("OPENAI_API_KEY"),  # Get from .env
    model=os.getenv("OPENAI_MODEL", "gpt-4"),  # Default to gpt-4 if not set
    api_base=os.getenv("OPENAI_API_BASE", "https://openai.vocareum.com/v1")
)

# Load CSV with standard pandas functionality
df = pdp.read_csv("testsales.csv")

# Run a prompt
print(df.prompt("Show me the top 5 rows according to the Total Profit"))
#print(df.prompt("Show me the top 5 rows according to the Total Profit").prompt("calculate the avearge Total profit"))