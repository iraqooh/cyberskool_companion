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

4. Run the Application (Dev Mode)

```bash
python app.py
```

Access the Web UI at: http://localhost:5000/

## 📥 API Usage

### POST /summarize

Headers:
```bash
Content-Type: application/json 
OR 
Content-Type: multipart/form-data
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
model: facebook/bart-large-cnn (optional and TBD)
```

Response:
```json
{
  "status": "OK",
  "data": "This is the AI-generated summary of your content."
}
```

### GET /health

Returns status of the application.

```json
{ "status": "ok" }
```

## 🧠 Model

Uses sshleifer/distilbart-cnn-12-6 from Hugging Face Transformers, a simple encoder-decoder transformer architecture. Support for additional models will be extended and enable users to choose the model.

## 🗂️ Project Structure

```pgsql
cyberskool_companion/
├── app.py                  
├── summarizer.py    
├── utils/
├── templates/              
├── static/                 
├── docs/
├── tests/
├── requirements.txt
├── Dockerfile
├── nginx.conf
├── LICENSE
└── README.md
```

## 🐳 Docker (Production)

1. Build the image

```bash
docker build -t cyberskool_companion .
```

2. Run with Gunicorn

```bash
docker run -d -p 8000:8000 cyberskool_companion
```

3. NGINX Reverse Proxy

```ngnix
server {
    listen 80
    server_name IP;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## 📖 License

This project is licensed under the GNU General Public License v3.0.

You are free to use, modify, and distribute this software under the terms of the LICENSE file.

## 🙌 Credits

Built with:

- Hugging Face Transformers

- PyTorch

- Flask

- TailwindCSS

Inspired by open-source research in NLP & education technology

## ✉️ Contact

For questions or collaboration:
Mr. Harry Iraku — [LinkedIn](https://linkedin.com/iraqooh) | [GitHub](https://github.com/iraqooh/)
