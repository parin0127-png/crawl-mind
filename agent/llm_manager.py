import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from openai import OpenAI, RateLimitError
from dotenv import load_dotenv
from rich.console import Console
import time

console = Console()

client = OpenAI(api_key = os.getenv("MISTRAL_API_KEY"),
                base_url = "https://api.mistral.ai/v1")

MODEL_PRIORITY = [
    "mistral-large-latest",
    "mistral-small-latest",
    "open-mistral-nemo",
    "codestral-latest",
    "open-mixtral-8x7b",
    "mistral-medium-latest",
]

def safe_llm(messages, primary_model = None):
    models_to_try = MODEL_PRIORITY.copy()
    if primary_model and primary_model in models_to_try:
        models_to_try.remove(primary_model)
        models_to_try.insert(0 , primary_model)

    for model in models_to_try:
        for attempt in range(2):
            try:
                response = client.chat.completions.create(
                    model = model,
                    messages = messages
                )
                return response.choices[0].message.content
            except RateLimitError:
                console.print(f"[red] ● [/red] [dim] Model {model} busy (429). Retrying/Switching... [/dim]")
                time.sleep(2)
            except Exception as e:
                console.print(f"[red] ● [/red] [dim] Error with {model}: {str(e)} [/dim]")
                break
    raise Exception("Critical: All Mistral models are currently reaching capacity.")
    