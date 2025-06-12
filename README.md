# 🤖 Cyberskool Companion — AI Text Summarizer

**Cyberskool Companion** is a lightweight, API-first AI Text Summarizer built using Python, Hugging Face Transformers, PyTorch, and Flask. It empowers users to extract concise summaries from long-form documents with a RESTful interface and pre-trained NLP models.

Designed to be easy to integrate into educational tools, research dashboards, or internal content curation platforms.

## ✨ Features

- 📄 **Extractive and Abstractive Summarization**
- 📏 **Length Control** — choose short, medium, or long summaries
- 📁 **File Input Support** — summarize `.txt`, `.pdf`, `.docx` or raw text
- 🌐 **RESTful API** — use with any frontend or backend system
- 🔐 **Basic Security** — input validation and request limits
- 🧠 **Powered by BART** — state-of-the-art transformer model

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/iraqooh/cyberskool_companion.git
cd cyberskool_companion
```

2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

4. Run the Application

```bash
python app.py
```

Access the summarizer at: http://localhost:5000/summarize

## 📥 API Usage

### POST /summarize

Headers:
```bash
Content-Type: application/json OR multipart/form-data
```

Body Options:
Text input (JSON):
```json
{
  "text": "Paste your long article here...",
  "length": "short" // options: short, medium, long
}
```

File input (form-data):
```vbnet
file: <uploaded .pdf/.docx/.txt file>
length: short|medium|long
```

Response:
```json
{
  "summary": "This is the AI-generated summary of your content."
}
```

### GET /health

Returns status of the application.

## 🧠 Model

Uses facebook/bart-large-cnn from Hugging Face Transformers, a powerful encoder-decoder transformer architecture fine-tuned for summarization tasks.

## 🗂️ Project Structure

```pgsql
cyberskool-companion/
├── app.py                  # Flask application
├── summarizer.py           # Model loading & summarization
├── utils/
│   └── text_extractor.py   # File-to-text conversion
├── templates/              # (Optional) UI templates
├── static/                 # (Optional) CSS/JS for UI
├── requirements.txt
└── README.md
```

## 🐳 Docker

Create a Dockerfile to containerize the app.

```bash
docker build -t cyberskool-companion .
docker run -p 5000:5000 cyberskool-companion
```

## 📖 License

This project is licensed under the GNU General Public License v3.0.

You are free to use, modify, and distribute this software under the terms of the LICENSE file.

## 🙌 Credits

Built with Hugging Face Transformers

Inspired by open-source research in NLP & education technology

## ✉️ Contact

For questions or collaboration:
Mr. Harry Iraku — (LinkedIn)[https://linkedin.com/iraqooh] | (GitHub)[https://github.com/iraqooh/]
