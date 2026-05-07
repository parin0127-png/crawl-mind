import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dotenv import load_dotenv

from llm_manager import safe_llm

load_dotenv()

def analysis(scraped_data, competitor_data, rag_guidelines):
    prompt = f"""You are an expert SEO analyst. Please review the following report brief and provide a detailed analysis.

    ### Here is the scraped SEO data:
    {scraped_data}

    ### Here are the competitor results:
    {competitor_data}

    ### Here are the relevant SEO guidelines:
    {rag_guidelines}

    ### Instructions:
    Analyze all the provided information above. Based on the scraped data, competitor benchmarks, and the SEO guidelines, please return a structured report that includes:
    1. Identified Issues: A clear description of each SEO problem found.
    2. Priority Level: Assign a priority (e.g., High, Medium, Low) to each issue based on its potential impact.
    3. Action Items: Specific, actionable steps required to fix each issue.
"""

    messages = [{"role" : "user" , "content" : prompt}]
    text = safe_llm(messages, primary_model = "mistral-large-latest")
    return text