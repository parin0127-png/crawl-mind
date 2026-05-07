import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agent.pipelines.RAG.retriever import load_knowledge_base, retriever

def run(scraped_data):
    index, chunks = load_knowledge_base()

    queries = []
    if scraped_data.get("missing_alt", 0) > 0:
        queries.append("images missing alt text")

    if not scraped_data.get("meta_description", ""):
        queries.append("meta description missing")

    if scraped_data.get("word_count", 0) < 300:
        queries.append("low word count thin content")

    results = []
    for q in queries:
        results.extend(retriever(q, index, chunks))

    return results