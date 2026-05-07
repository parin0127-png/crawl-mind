import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from pipelines.scraper_stage import run as scraper
from pipelines.competitor_stage import run as competitor
from pipelines.rag_stage import run as rag
from pipelines.analysis_stage import analysis
from pipelines.output_stage import run as output
from dotenv import load_dotenv
from openai import OpenAI, RateLimitError
from llm_manager import safe_llm
import time

from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich import print as rprint

load_dotenv()

console = Console()

system_prompt = """
        You are an SEO agent. Your job is to analyze a website completely.

        You have these tools available:
        - scraper: scrapes the website and returns SEO data like title, headings, meta description, word count, image issues
        - competitor: searches the web for competitor websites and returns their titles, URLs, and summaries
        - rag: retrieves SEO guidelines from the knowledge base based on scraped data issues

        Rules:
        - You must reply with ONLY one word
        - No explanations, no extra text, just one word
        - Choose from: scraper, competitor, rag, analyze, done
        - If scraper data is missing, run scraper first
        - If competitor data is missing, run competitor next
        - If rag data is missing, run rag next
        - Once you have all three, say analyze
        - Never repeat a tool you already ran
"""


def run_agent(url):
    console.print(Rule("[bold cyan]● CrawlMind SEO Agent ●[/bold cyan]", style="cyan"))
    console.print(Panel(f"[bold white]● Target URL:[/bold white] [cyan]{url}[/cyan]", style="dim"))

    index_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pipelines", "RAG", "markdown.index")
    if not os.path.exists(index_path):
        console.print("[yellow]⚙  Building knowledge base for first time...[/yellow]")
        from pipelines.RAG.embedding import load_documents, chunk_doc, embed_chunks, save_to_faiss
        doc = load_documents()
        chunks = chunk_doc(doc)
        vector = embed_chunks(chunks)
        save_to_faiss(vector, chunks)
        console.print("[green]●[/green]  Knowledge base ready.")
        console.print(Rule(style="dim"))

    collected_data = {}
    step = 0

    while step < 10:
        user_message = f"URL : {url} \n Data collected so far : {list(collected_data.keys())}\n What to do next ?"

        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
                

        answer = safe_llm(messages, primary_model = "open-mistral-nemo").strip().lower()

        if answer == "scraper":
            console.print("[dim]●[/dim]  Running [bold]scraper[/bold]...")
            collected_data["scraper"] = scraper(url)
            console.print("[green]●[/green]  Scraper completed.")
            console.print(Rule(style="dim"))

        elif answer == "competitor":
            console.print("[dim]●[/dim]  Running [bold]competitor search[/bold]...")
            collected_data["competitor"] = competitor(url)
            console.print("[green]●[/green]  Competitor search done.")
            console.print(Rule(style="dim"))

        elif answer == "rag":
            console.print("[dim]●[/dim]  Running [bold]RAG retrieval[/bold]...")
            collected_data["rag"] = rag(collected_data["scraper"])
            console.print("[green]●[/green]  RAG retrieval complete.")
            console.print(Rule(style="dim"))

        elif answer in ("analyze", "done"):
            break

        else:
            console.print(f"[dim]  Mistral → {answer}[/dim]")

        step += 1

    if "scraper" not in collected_data or "competitor" not in collected_data or "rag" not in collected_data:
        console.print("[yellow]●  Missing data — re-running missing tools...[/yellow]")
        if "scraper" not in collected_data:
            console.print("[dim]●[/dim]  Re-running [bold]scraper[/bold]...")
            collected_data["scraper"] = scraper(url)
            console.print("[green]●[/green]  Scraper completed.")
        if "competitor" not in collected_data:
            console.print("[dim]●[/dim]  Re-running [bold]competitor search[/bold]...")
            collected_data["competitor"] = competitor(url)
            console.print("[green]●[/green]  Competitor search done.")
        if "rag" not in collected_data:
            console.print("[dim]●[/dim]  Re-running [bold]RAG retrieval[/bold]...")
            collected_data["rag"] = rag(collected_data["scraper"])
            console.print("[green]●[/green]  RAG retrieval complete.")
        console.print(Rule(style="dim"))

    console.print("[dim]●[/dim]  Running [bold]analysis[/bold]...")
    analysis_result = analysis(collected_data["scraper"], collected_data["competitor"], collected_data["rag"])
    import io, contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        md_path, html_path, pdf_path = output(collected_data["scraper"], analysis_result)

    console.print(Rule(style="dim"))
    completion_text = (
        "[bold #F5BF4F]● CrawlMind agent complete.[/bold #F5BF4F]\n\n"
        f"[#F5BF4F]Markdown save  ->  {md_path}[/#F5BF4F]\n"
        f"[#F5BF4F]HTML save      ->  {html_path}[/#F5BF4F]\n"
        f"[#F5BF4F]Pdf save       ->  {pdf_path}[/#F5BF4F]"
    )
    console.print(Panel(completion_text, style="#F5BF4F"))