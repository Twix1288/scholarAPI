# main.py
from fastapi import FastAPI, Request, HTTPException
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from arxiv import search_arxiv
from summarizer import summarize_text
from citation import generate_citation
from dotenv import load_dotenv

load_dotenv()

limiter = Limiter(key_func=get_remote_address)

app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/api/search")
@limiter.limit("5/minute")
def search(query: str, limit: int = 5):
    return search_arxiv(query, limit)

@app.get("/api/summarize")
@limiter.limit("10/minute")
def summarize(
    request: Request,
    text: str,
    length: str = "short"
):
    return {"summary": summarize_text(text, length)}

@app.get("/api/citation")
def citation(
    request: Request,
    title: str,
    authors: str,
    published: str
):
    author_list = authors.split(",")
    return {"citation": generate_citation(title, author_list, published)}
