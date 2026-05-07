from tavily import TavilyClient
from dotenv import load_dotenv
import os 

load_dotenv()
client = TavilyClient(api_key = os.getenv("TAVILY_API_KEY"))
def search(message , max_results = 5):
    full_result = []
    try : 
        result = client.search(message, max_results = max_results)
        for r in result["results"]:
            if "icon" in r["content"] and "media" in r["content"]:
                continue
            full_result.append({"title" : r["title"] , "url" : r["url"] , "content" : r["content"]})

        return full_result
    except Exception as e :
        return f"Error in search : {e}"

