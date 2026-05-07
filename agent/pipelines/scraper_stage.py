import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools.web_scraper import web_scraper
def run(url):
    result = web_scraper(url)
    return result
