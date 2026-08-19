# 🔬 Multi-Agent AI Research System

A modular multi-agent research pipeline built with **LangChain**, **Mistral AI**, **Tavily Search**, and **BeautifulSoup**.

The system coordinates specialized AI agents to search the web, identify relevant sources, scrape detailed content, generate a structured research report, and critically evaluate the final output.

## ✨ Features

- 🔎 Searches the web for recent and relevant information
- 🌐 Retrieves source titles, URLs, and content snippets
- 📖 Selects and scrapes relevant web resources
- ✍️ Generates structured research reports
- 🧠 Reviews reports using an AI critic
- 🔗 Preserves source URLs for traceability
- 🤖 Uses specialized agents for separate research tasks
- 🧩 Implements a modular and extensible pipeline architecture

## 🏗️ Architecture

```text
User Research Topic
        │
        ▼
┌─────────────────────┐
│    Search Agent     │
│   Mistral Medium    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│     Web Search      │
│       Tavily        │
└──────────┬──────────┘
           │
           │ Titles + URLs + Snippets
           ▼
┌─────────────────────┐
│    Reader Agent     │
│   Mistral Medium    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│     URL Scraper     │
│ BeautifulSoup +     │
│ Requests            │
└──────────┬──────────┘
           │
           │ Detailed Content
           ▼
┌─────────────────────┐
│    Writer Chain     │
│ Structured Report   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    Critic Chain     │
│ Quality Evaluation  │
└──────────┬──────────┘
           │
           ▼
     Final Feedback
```

## 🤖 Agent Responsibilities

### 1. Search Agent

The Search Agent receives a research topic and uses the Tavily-powered `web_search` tool to find recent and reliable information.

Example:

```text
Topic:
Impact of war on the stock market
```

The search tool returns:

```text
Title: Example Article
URL: https://example.com/article
Description: Relevant content snippet...
```

Raw tool outputs are extracted from LangChain `ToolMessage` objects so that source URLs are preserved for downstream processing.

### 2. Reader Agent

The Reader Agent receives:

- The original research topic
- Search result titles
- Source URLs
- Content snippets

It selects a relevant URL and invokes the `scrape_url` tool for deeper reading.

The scraper uses:

- `requests`
- `BeautifulSoup`

It removes unnecessary HTML elements such as:

```text
script
style
nav
footer
```

and extracts readable page content.

### 3. Writer Chain

The Writer Chain combines:

```text
Search Results
      +
Detailed Scraped Content
```

It generates a structured report containing:

- Introduction
- Key Findings
- Conclusion
- Sources

### 4. Critic Chain

The Critic Chain evaluates the generated report and returns:

```text
Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
...
```

## 🔄 Pipeline Flow

```text
User Topic
    ↓
Search Agent
    ↓
Tavily Web Search
    ↓
Raw ToolMessage Extraction
    ↓
Search Results + URLs
    ↓
Reader Agent
    ↓
URL Selection
    ↓
BeautifulSoup Scraping
    ↓
Detailed Content
    ↓
Writer Chain
    ↓
Structured Research Report
    ↓
Critic Chain
    ↓
Score + Feedback
```

## 📁 Project Structure

```text
Multi_agent/
│
├── agents.py
├── tools.py
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

### `tools.py`

Contains the custom research tools:

```python
web_search()
scrape_url()
```

### `agents.py`

Contains:

```python
build_search_agent()
build_reader_agent()
writer_chain
critic_chain
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd multi-agent-research-system
```

### 2. Create a virtual environment

Using `uv`:

```bash
uv venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
uv pip install -r requirements.txt
```

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
```
The pipeline will:

1. Search the web
2. Select and scrape a relevant source
3. Generate a research report
4. Review and score the report

## Future Improvements

- Multi-source scraping
- Citation validation
- Fact-checking agent
- LangGraph workflow
- Async parallel research
- Streamlit or FastAPI interface

## License

This project is intended for educational and research purposes.



