import os
from dotenv import load_dotenv
def setup():
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")

    load_dotenv(env_path)
    tavily = os.getenv("TAVILY_API_KEY", "")
    mistral = os.getenv("MISTRAL_API_KEY", "")

    if not tavily or not mistral:
        print("+-" * 30)
        print("> First time setup. Please enter your API keys.")
        print("+-" * 30)
        print("> You need two free API keys to use CrawlMind.")
        print("> ")
        print("> 1. Tavily API Key  -> Sign up free at: https://tavily.com")
        print(">    Used for: Competitor research and web search")
        print("> ")
        print("> 2. Mistral API Key -> Sign up free at: https://console.mistral.ai")
        print(">    Used for: AI analysis and planning")
        print("> ")
        print("+-" * 30)

        tavily = input("> Enter tavily API key : ").strip()
        mistral = input("> Enter mistral API key : ").strip()

        with open(env_path , "w")as f:
            f.write(f'TAVILY_API_KEY = "{tavily}"\n')
            f.write(f'MISTRAL_API_KEY = "{mistral}"')

        load_dotenv(env_path)
        print("> API keys saved successfully.")
        print("+-" * 30)

if __name__ == "__main__":
    setup()
    print("> Setup complete. Now run: python main.py")
    