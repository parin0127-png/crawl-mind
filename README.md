# CrawlMind 🕷️

> AI-powered SEO analysis agent that audits any website and generates a full report automatically.

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg) &nbsp; ![Python](https://img.shields.io/badge/Python-3.10+-blue.svg) &nbsp; ![Mistral AI](https://img.shields.io/badge/LLM-Mistral%20AI-orange.svg) &nbsp; ![RAG](https://img.shields.io/badge/Architecture-RAG-green.svg)

---

## 🚀 What is CrawlMind?

CrawlMind is an agentic SEO tool built in Python. You give it a URL, and it takes care of everything — scraping the page, researching competitors, pulling relevant SEO guidelines from a local knowledge base, running an AI analysis, and saving the results as a Markdown file, an HTML dashboard, and a PDF report.

The agent is powered by Mistral AI and decides on its own which tool to run at each step.

---

## ✨ How it works

1. **Scrapes the target website** — extracts title, H1/H2/H3 headings, meta description, image count, missing alt tags, and word count
2. **Searches for competitors** — uses Tavily to find competitor websites related to the target URL
3. **Retrieves SEO guidelines** — queries a local FAISS vector database built from curated SEO markdown files to find the most relevant guidelines based on the issues found
4. **Runs AI analysis** — sends all collected data to Mistral AI and gets back a structured report with identified issues, priority levels, and action items
5. **Saves the output** — generates an interactive HTML dashboard with charts, a Markdown report, and a PDF audit report

---

## ✅ Example URLs you can audit

- Any blog or news website
- E-commerce product or category pages
- Portfolio or personal websites
- SaaS landing pages
- Local business websites

---

## ⚡ Installation

**1. Clone the repository**

```bash
git clone https://github.com/parin0127-png/CrawlMind.git
cd CrawlMind
```

**2. Create a virtual environment**

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Install Playwright browser**

```bash
playwright install chromium
```

---

## 🔑 Setup

You need two free API keys:

- **Mistral API Key** — get it free at https://console.mistral.ai
- **Tavily API Key** — get it free at https://tavily.com

On first run, CrawlMind will automatically ask for these keys and save them to a `.env` file. You don't need to set anything up manually.

---

## ▶️ Run

```bash
python main.py
```

Then enter the target URL when prompted:

```
> Enter website URL : https://example.com
```

The agent will run all stages automatically and print live progress to the terminal. When done, it shows the paths to the three generated output files.

---

## 📁 Project Structure

```
CrawlMind/
├── agent/
│   ├── agent.py                  # Main agent loop
│   ├── llm_manager.py            # Mistral API wrapper with model fallback
│   ├── pipelines/
│   │   ├── scraper_stage.py      # Runs the web scraper
│   │   ├── competitor_stage.py   # Runs competitor search
│   │   ├── rag_stage.py          # Runs RAG retrieval
│   │   ├── analysis_stage.py     # Runs Mistral analysis
│   │   ├── output_stage.py       # Generates HTML dashboard and Markdown report
│   │   └── RAG/
│   │       ├── embedding.py      # Loads, chunks, embeds, and saves to FAISS
│   │       ├── retriever.py      # Loads FAISS index and retrieves chunks
│   │       ├── chunks.txt        # Stored text chunks
│   │       ├── markdown.index    # FAISS vector index
│   │       └── markdown/         # SEO knowledge base (markdown files)
│   └── tools/
│       ├── web_scraper.py        # BeautifulSoup + Playwright scraper
│       ├── searcher.py           # Tavily search wrapper
│       └── report_generator.py   # ReportLab PDF generator
├── output/                       # Generated reports saved here (git ignored)
├── main.py                       # Entry point
├── setup.py                      # First-time API key setup
├── .env                          # API keys (git ignored)
├── .gitignore
└── requirements.txt
```

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Mistral AI** — agent planning and SEO analysis
- **Tavily** — competitor and web search
- **FAISS** — local vector store for RAG
- **Sentence Transformers** — `all-MiniLM-L6-v2` for embeddings
- **BeautifulSoup + Playwright** — web scraping with JS fallback
- **ReportLab** — PDF generation
- **Chart.js** — charts in the HTML dashboard
- **Rich** — terminal UI

---

## 📊 Output Files

After a successful run, three files are saved in the `output/` folder:

- `SEO_REPORT_<timestamp>.md` — full AI-generated SEO analysis in Markdown
- `Dashboard_<timestamp>.html` — interactive dashboard with health score, charts, and full analysis
- `audit_report.pdf` — basic PDF with on-page metrics

---

## 📚 Knowledge Base

The RAG system is built from five hand-written SEO guides covering:

- On-page SEO (title tags, meta descriptions, heading structure, URL structure, internal linking)
- Technical SEO (Core Web Vitals, page speed, crawlability, sitemaps, schema markup)
- Content SEO (search intent, keyword density, thin content, duplicate content)
- Backlink SEO (link building strategies, anchor text, toxic backlinks)
- Google Algorithms (Panda, Penguin, Helpful Content System, E-E-A-T, YMYL)

On first run, the knowledge base is automatically embedded and saved as a FAISS index. This only happens once.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

MIT License — see [LICENSE](LICENSE) file for details.

---

## 👤 Author

Parin — [@parin0127-png](https://github.com/parin0127-png)

---

⭐ If you found this useful, please star the repo!
