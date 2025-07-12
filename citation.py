def generate_citation(title: str, authors: list, published: str):
    author_str = ", ".join(authors)
    return f"{author_str} ({published}). {title}. arXiv."