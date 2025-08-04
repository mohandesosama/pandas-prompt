# to make this code works locally, do the following 
# pip install -e .

import pandas_prompt as pdp

df = pdp.read_csv("Sales.csv")
result = df.prompt("Show rows where Total profit > 600000")
print(result)
