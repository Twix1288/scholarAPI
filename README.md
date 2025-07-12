# scholarAPI
A FastAPI api to pull research papers through keywords, summarize papers, and to get citations
📚 ScholarSearch API

An open-source research paper discovery and summarization API using the arXiv API, built with FastAPI and powered by OpenAI or Hugging Face for natural language summarization.

🚀 Features

🔍 Search academic papers by keyword using arXiv
📄 Retrieve metadata: title, abstract, authors, publication date, PDF link
🧠 Summarize abstracts or full papers using GPT-4o or BART (pluggable)
📎 Format citations in BibTeX (APA/MLA support coming soon!)
📉 Built-in rate limiting to prevent abuse
🔒 (Optional) API key authentication and per-user quotas (easy to add)
🛠️ Installation

git clone https://github.com/your-username/scholarsearch-api.git
cd scholarsearch-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Create a .env file based on the example:

cp .env.example .env
Edit .env and add your OpenAI API key:

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
🧪 Running the API

uvicorn main:app --reload
Visit http://localhost:8000/docs for interactive API docs (via Swagger UI).

🌐 API Endpoints

🔍 /api/search
Search arXiv by keyword.

Example:

GET /api/search?query=transformers&limit=5
🧠 /api/summarize
Summarize text using GPT.

Example:

GET /api/summarize?text=Deep%20learning%20is...&length=short
Query Params:

text – The content to summarize
length – short, medium, or long
📎 /api/citation
Generate a simple citation string.

Example:

GET /api/citation?title=AI%20and%20Robotics&authors=Alice,Bob&published=2023-05-01
📦 File Structure

scholarsearch-api/
├── main.py            # FastAPI app and routes
├── rarxiv.py          # arXiv search wrapper
├── summarizer.py      # Summarization logic (GPT or BART)
├── citation.py        # Citation formatting
├── requirements.txt   # Dependencies
├── .env.example       # API key config template
├── README.md          # Project documentation
✅ To-Do (Future Improvements)

 Add support for HuggingFace Transformers (BART/PEGASUS)
 Format citations in APA and MLA
 Add /register endpoint to generate API keys
 Add usage quotas and tracking
 Deploy to Render, Vercel, or Hugging Face Spaces
📄 License

This project is licensed under the MIT License.

🤝 Contributions

Pull requests are welcome! If you’d like to contribute:

Fork the repo
Make your changes
Submit a PR
Let’s build a better way to search and understand research 📚


