import warnings
warnings.filterwarnings("ignore")
import os 
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["TRANSFORMERS_VERBOSITY"] = "error"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"
os.environ["TQDM_DISABLE"] = "1"
os.environ["TRANSFORMERS_NO_ADVISORY_WARNINGS"] = "1"
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import logging
logging.getLogger("sentence_transformers").setLevel(logging.ERROR)
logging.getLogger("transformers").setLevel(logging.ERROR)
logging.getLogger("huggingface_hub").setLevel(logging.ERROR)


def load_knowledge_base():
    base = os.path.dirname(os.path.abspath(__file__))
    index = faiss.read_index(os.path.join(base, "markdown.index"))
    with open(os.path.join(base,"chunks.txt") , "r") as f:
        content = f.read()
        chunks = content.split("\n-----\n")
    return index , chunks

model = SentenceTransformer("all-MiniLM-L6-v2")
def retriever(query , index , chunks):
    query = np.array([model.encode(query)]).astype("float32")
    distance, indices = index.search(query,5)
    result = [chunks[i] for i in indices[0]]
    return result
