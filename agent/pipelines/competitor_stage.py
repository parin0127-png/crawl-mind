import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools.searcher import search

def run(message):
    result = search(message)
    return result

