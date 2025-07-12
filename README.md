readme_content = """
# scholarAPI

A FastAPI API to pull research papers through keywords, summarize papers, and get citations

📚 **ScholarSearch API**

An open-source research paper discovery and summarization API using the arXiv API, built with FastAPI and powered by OpenAI or Hugging Face for natural language summarization.

---

## 🚀 Features

- 🔍 Search academic papers by keyword using arXiv  
- 📄 Retrieve metadata: title, abstract, authors, publication date, PDF link  
- 🧠 Summarize abstracts or full papers using GPT-4o or BART (pluggable)  
- 📎 Format citations in BibTeX (APA/MLA support coming soon!)  
- 📉 Built-in rate limiting to prevent abuse  
- 🔒 (Optional) API key authentication and per-user quotas (easy to add)  

---

## 🛠️ Installation

```bash
git clone https://github.com/your-username/scholarsearch-api.git
cd scholarsearch-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
