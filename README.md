# 🧠 pandas-prompt

[![version](https://img.shields.io/badge/version-0.1.0-blue.svg)](https://github.com/mohandesosama/pandas-prompt)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![pandas](https://img.shields.io/badge/pandas-compatible-brightgreen)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Issues](https://img.shields.io/github/issues/mohandesosama/pandas-prompt.svg)](https://github.com/mohandesosama/pandas-prompt/issues)
[![Stars](https://img.shields.io/github/stars/mohandesosama/pandas-prompt.svg?style=social)](https://github.com/mohandesosama/pandas-prompt)

> ✨ Natural language interface for pandas using LLMs. Extend `DataFrame` with `.prompt()` to talk to your data.

---

## 🚀 Overview

`pandas-prompt` is a natural-language interface to the full power of `pandas`.  
It extends `pandas` by adding a `.prompt()` method to any `DataFrame`, letting you write natural language instructions like:

```python
df.prompt("Show the average sales for each department")
```

This is powered by a local or remote LLM (e.g., OpenAI API), which converts the prompt into executable Python code using the DataFrame as `df`.

---

## Key Use Cases

### 1. Natural Language Data Querying
- Interactive Analysis: Execute natural language queries directly against datasets
- Ad-hoc Exploration: Investigate patterns and relationships through conversational prompts
- Example: 
  ```python
  df.prompt("Show products with highest profit margin in Q4")
  ```
### 2. Dynamic Pattern Visualization
- Real-time Insights: Generate dynamically updating visualizations that reflect live data patterns

- Visual Validation: Create responsive graphs that automatically update when underlying data changes

- Workflow:

```python
result = df.prompt("Visualize monthly sales trends")
result.plot()  # Auto-updates when data refreshes
```
### 3. Iterative Analysis Workflow
- Chained Exploration: Conduct follow-up queries on transformed DataFrames from previous operations

- Contextual Investigation: Maintain analysis context across multiple prompt interactions

Example:

```python
filtered = df.prompt("Show records from California")
filtered.prompt("Compare revenue by product category")
```
## 📦 Installation

1. Clone the repo:

```bash
git clone https://github.com/yourusername/pandas-prompt.git
cd pandas-prompt
```

2. Install locally in development mode:

```bash
pip install -e .
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install pandas openai python-dotenv
```

---

## 🔐 Environment Setup

Create a `.env` file in the `pandas_prompt/` directory or project root:

```
OPENAI_API_KEY=your_key_here
```

To use with a custom OpenAI-compatible endpoint (e.g., Vocareum):

```python
self.client = OpenAI(
    base_url="openai url here",
    api_key=os.getenv("OPENAI_API_KEY")
)
```

---

## 🧪 Example Usage

```python
import pandas_prompt as pdp

df = pdp.read_csv("examples/Sales.csv")

# Ask a question in natural language
result = df.prompt("Show rows where Sales > 1000")
print(result)

print(df.prompt("Show me the top 5 rows according to the Total Profit").prompt("calculate the avearge Total profit"))
# output is 6454.54
```

📌 The `.prompt()` method prints the generated code and returns the result of execution (if any).

---

## ✅ Planned Features

- ✅ Full pandas compatibility
- ✅ Basic natural language prompt support
- ✅ Offline support (e.g., Mistral with `llama-cpp`)
- ✅ `.prompt_plot()` for visualization tasks
- 🔄 Multi-turn `.chat()` mode with memory
- 📁 PyPI packaging + GitHub Actions

---

## 🤝 Contributing

Pull requests and issue reports are welcome!  
To contribute:

```bash
git checkout -b my-feature
# make changes
git commit -am "Add new feature"
git push origin my-feature
```

---

## 📜 License

This project is licensed under the MIT License — see the `LICENSE` file for details.
