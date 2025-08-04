from setuptools import setup, find_packages

setup(
    name="pandas-prompt",
    version="0.1.0",
    description="Natural language prompts for pandas DataFrames",
    author="Osama Hosameldeen",
    packages=find_packages(),
    install_requires=["pandas>=1.0", "openai>=1.0"],
    python_requires=">=3.7",
)