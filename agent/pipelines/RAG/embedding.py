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

def load_documents():
    doc = os.path.join(os.path.dirname(os.path.abspath(__file__)), "markdown")
    doc_list = os.listdir(doc)
    list_doc = []
    for d in doc_list:
        if d.endswith(".md"):
            full_path = os.path.join(doc , d)
            with open(full_path, "r") as f:
                content = f.read()
            list_doc.append((content, d))
    return list_doc

def chunk_doc(list_doc):
    chunks = []
    for content, filename in list_doc:
        paragraph = content.split("\n\n")
        for p in paragraph:
            if len(p) > 50:
                chunks.append((p, filename))
    return chunks
model = SentenceTransformer("all-MiniLM-L6-v2")
def embed_chunks(chunks):
    texts = [chunk[0] for chunk in chunks]
    vector = model.encode(texts, show_progress_bar = False)
    return vector

def save_to_faiss(vector, chunks):
    base = os.path.dirname(os.path.abspath(__file__))
    vector = np.array(vector).astype("float32")
    index = faiss.IndexFlatL2(vector.shape[1])
    index.add(vector)

    faiss.write_index(index, os.path.join(base, "markdown.index"))

    texts = [chunk[0] for chunk in chunks]
    with open(os.path.join(base,"chunks.txt") , "w")as f:
        for text in texts:
            f.write(text + "\n-----\n")

