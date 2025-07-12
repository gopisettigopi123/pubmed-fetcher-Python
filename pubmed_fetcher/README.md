# PubMed Fetcher

Your task is to write a Python program to fetch research papers based on a user-specifiedquery.The
program must identify papers with at least one author affiliated with a pharmaceutical or biotech
company and return the results as a CSV file.

## Overview

A command-line tool to fetch PubMed articles with at least one author affiliated with a pharmaceutical or biotech company.

## Features

- Fetches articles using PubMed API
- Filters for non-academic authors using keyword heuristics
- Outputs to CSV or terminal
- Includes debug and help options
- Packaged with Poetry and ready to publish

## Installation

````bash
git clone https://github.com/gopisettigopi123/pubmed-fetcher-Python.git
cd pubmed-fetcher
poetry install

poetry run get-papers-list "cancer treatment" -f output.csv -d

## 📁 Project Structure
pubmed_fetcher/
│
├── pubmed_fetcher/ # Main module package
│ ├── init.py
│ ├── cli.py # CLI entry point
│ ├── fetch.py # PubMed API logic
│ ├── filters.py # Non-academic filter logic
│ └── utils.py # CSV and helper functions
│
├── tests/ # Unit tests (optional)
│
├── pyproject.toml # Poetry project and dependency config
├── README.md # Project documentation
└── output.csv # Example output file (ignored by .gitignore)

## ⚙️ Features

- ✅ Search PubMed via official API
- ✅ Filter for **non-academic authors** using text heuristics
- ✅ Save results to a **CSV** file or print to terminal
- ✅ Optional `--debug` mode for internal logging
- ✅ Clean modular Python code with type annotations
- ✅ Easily extendable for year-based or keyword-based filtering

## 💻 Installation

> 📌 Requires **Python 3.8+** and **Poetry**

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pubmed-fetcher.git
cd pubmed-fetcher

2. Install Poetry (if not already installed)
bash
Copy
Edit
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
Ensure Poetry is accessible:

bash
Copy
Edit
poetry --version

3. Install Dependencies
bash
Copy
Edit
poetry install

Usage
Basic Query:
bash
Copy
Edit
poetry run get-papers-list "cancer treatment"

Save to CSV:
bash
Copy
Edit
poetry run get-papers-list "diabetes drugs" -f diabetes.csv
Enable Debug Mode:
bash
Copy
Edit
poetry run get-papers-list "gene therapy" -f output.csv -d
poetry run get-papers-list "cancer treatment" -f cancer_results.csv -d


🧠 How Non-Academic Authors Are Identified
We use a simple heuristic that:

✅ Includes affiliations with keywords like pharma, biotech, inc, corp, therapeutics, etc.

❌ Excludes affiliations with keywords like university, college, institute, school, etc.

This method is not perfect, but works well for practical filtering.


🛠 Tools & Libraries Used
Tool	Purpose	Link
Poetry	Dependency and packaging manager	https://python-poetry.org
Requests	HTTP client to call PubMed API	https://requests.readthedocs.io
pandas	For writing structured CSVs	https://pandas.pydata.org
argparse	CLI argument parser	Standard Library
tqdm	Progress bars (optional)	https://tqdm.github.io/
🧠 This project was enhanced with the help of ChatGPT (LLM from OpenAI) for generation and refactoring suggestions.
🔐 License
This project is licensed under the MIT License.

🙋‍♂️ Author
Gopi – LinkedIn
Feel free to fork, contribute, or reach out for improvements!
````
