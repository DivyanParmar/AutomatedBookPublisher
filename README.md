# 📚 AutomatedBookPublisher

**AutomatedBookPublisher** is a fully automated pipeline that scrapes a book chapter from the web, rewrites it using local AI models, enables human edits, and stores all versions for future semantic search. It’s ideal for digital publishers, educational platforms, and AI content workflows.

---

## 🚀 Features

- 🔗 **URL Scraping**: Fetch content from web pages
- 🖼️ **Webpage Screenshot**: Save original page as image
- 🤖 **AI-Powered Rewriting**: Rewrite content with free/local AI
- 🧠 **AI Review**: Refine output using a second AI pass
- ✍️ **Human-in-the-loop Editing**: Edit AI outputs manually
- 🧾 **Version History**: Save all stages for traceability
- 🔍 **Semantic Search**: Search across versions using ChromaDB

---

## 🛠️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/AutomatedBookPublisher.git
cd AutomatedBookPublisher
```

### 2. Set Up Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate       # macOS/Linux
# .\venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
playwright install
```

---

## ▶️ Usage

Run the entire pipeline with:

```bash
python -m src.cli chapter1 https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1
```

You will go through these steps:

1. Web scrape the content and save a screenshot
2. Automatically rewrite the text with AI
3. Manually edit `output/spun.txt`
4. AI reviews the human-edited version
5. Manually review `output/reviewed.txt`
6. Final version saved as `output/final.txt`

---

## 📁 Project Structure

```
AutomatedBookPublisher/
├── src/
│   ├── scraper.py       # Web scraping logic
│   ├── ai_agents.py     # AI rewrite & review
│   ├── versioning.py    # Save and index versions
│   └── cli.py           # Command-line runner
├── output/              # Stores output files
├── requirements.txt     # Python packages
└── README.md            # This file
```

---

## 🧼 .gitignore

Create a `.gitignore` file with:

```
venv/
__pycache__/
*.pyc
.chromadb/
.DS_Store
```

---

## ⚙️ Technologies Used

- Python 3.8+
- Playwright (for web scraping and screenshots)
- Hugging Face Transformers (local AI)
- ChromaDB (for vector-based storage and search)

---

## 📌 Notes

- No OpenAI or other paid APIs are used
- Works offline with local models
- Designed for transparency and human oversight
- Future features may include multi-chapter processing and UI

---

## 👤 Author

**Divyan Parmar**  
[GitHub](https://github.com/DivyanParmar) — *Feel free to fork, star, or contribute!*

---

## 📜 License

This project is open source under the [MIT License](LICENSE).
