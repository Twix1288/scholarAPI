import arxiv

def search_arxiv(query: str, limit: int = 5):
    results = arxiv.Search(
        query=query,
        max_results=limit,
        sort_by=arxiv.SortCriterion.Relevance
    )

    papers = []
    for result in results.results():
        papers.append({
            "title": result.title,
            "summary": result.summary,
            "authors": [a.name for a in result.authors],
            "pdf_url": result.pdf_url,
            "published": result.published.strftime("%Y-%m-%d")
        })

    return papers
