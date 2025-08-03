
# 📊 pandas-prompt

**Version**: `0.1.0`  
**Language**: Python 3.7+  
**License**: MIT  
**Author**: *Osama Hosameldeen*  
**LLM Backend**: OpenAI-compatible
**Dependencies**: `pandas`, `openai`, `python-dotenv`

---

## 🚀 Overview

`pandas-prompt` is a natural-language interface to the full power of `pandas`.  
It extends `pandas` by adding a `.prompt()` method to any `DataFrame`, letting you write natural language instructions like:

```python
df.prompt("Show the average sales for each department")
```

This is powered by a local or remote LLM (e.g., OpenAI API), which converts the prompt into executable Python code using the DataFrame as `df`.

---

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
    base_url="https://openai.vocareum.com/v1",
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
```

📌 The `.prompt()` method prints the generated code and returns the result of execution (if any).

---

## 🧠 How It Works

- Sample 10 rows from the DataFrame
- Construct a prompt: *“Given this DataFrame: [...], do: [instruction]”*
- Send to the OpenAI-compatible API
- Parse and execute the returned Python code in a local sandbox

---

## 🔧 Project Structure

```
pandas-prompt/
├── pandas_prompt/
│   ├── __init__.py         ← auto-patches pandas on import
│   ├── prompt.py           ← PromptEngine + .prompt() logic
│   ├── patch.py            ← (optional) manual patch logic
│   ├── .env                ← stores your API key
├── examples/
│   ├── demo.py             ← sample usage
│   └── Sales.csv           ← sample dataset
├── requirements.txt
├── setup.py
├── README.md
```

---

## 📌 Limitations

- Generated code is executed using `exec()` — avoid unsafe prompts
- Only supports `df.prompt(...)` (multi-turn not yet implemented)
- LLM quality depends on prompt and model used

---

## ✅ Planned Features

- ✅ Basic natural language prompt support
- 🔄 Offline support (e.g., Mistral with `llama-cpp`)
- 📊 `.prompt_plot()` for visualization tasks
- 🧠 Multi-turn `.chat()` mode with memory
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
