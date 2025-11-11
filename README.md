# 🗼 AI Paris Travel Chatbot

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-green.svg)](https://platform.openai.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Project Type](https://img.shields.io/badge/Type-Portfolio%20Project-orange.svg)](https://github.com/Johnnysnipes90)

An **AI-powered virtual tour guide** built with the **OpenAI API**, designed to deliver smart, engaging, and informative responses to common Paris travel questions.  
Developed as part of **Peterman Reality Tours’ AI Innovation Series**.

---

## 🚀 Features

- ✅ Built with **GPT-4o-mini** (efficient & accurate)  
- ✅ Preloaded with sample tourist questions  
- ✅ Fully **interactive CLI chat**  
- ✅ JSON-based conversation logging  
- ✅ Styled terminal UI using **Rich**  
- ✅ Secure `.env` API key handling  
- ✅ Strong error handling & clean modular code  
- ✅ **Docker + Docker Compose support**  
- ✅ Industry-standard project structure  

---

## 🧰 Project Structure



```
Paris-Travel-Chatbot/
├── src/
│ └── paris_chatbot.py
├── data/
│ └── conversation_log.json # created at runtime
├── .env.example
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
├── README.md
├── .gitignore
└── LICENSE
```

---

# ⚙️ **Local Setup (Without Docker)**

## 🧑‍💻 Setup & Run Locally

### 1) Clone the Repository
```bash
git clone https://github.com/Johnnysnipes90/Paris-Travel-Chatbot.git
cd Paris-Travel-Chatbot
```

2) **Create and activate a virtual environment**

```bash
# macOS/Linux
python3 -m venv .venv && source .venv/bin/activate

# Windows (Git Bash)
source .venv/Scripts/activate

# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3) **Install dependencies**
```bash
pip install -r requirements.txt
```

4) **Set your OpenAI API key**
```bash
# macOS/Linux
export OPENAI_API_KEY="your_api_key_here"

# Windows (Git Bash)
export OPENAI_API_KEY="your_api_key_here"

# Windows (PowerShell)
setx OPENAI_API_KEY "your_api_key_here"
$env:OPENAI_API_KEY="your_api_key_here"
```

(Optional) Create a .env file with:
```bash
OPENAI_API_KEY=your_api_key_here
MODEL_NAME=gpt-4o-mini
LOG_FILE_PATH=./data/conversation_log.json
```

5) **Run the Chatbot**
```bash
python src/paris_chatbot.py
```


# **🐳 Docker Setup (Production Ready)**

This project includes full Docker and Docker Compose support.

1) **Build the Docker image**
```bash
docker compose build
```

2) **Run the chatbot inside Docker**
```bash
docker compose up
```
- ✅ The data/ folder is persisted
- ✅ The .env file injects your OpenAI key
- ✅ Terminal stays interactive

3) **Stop the chatbot container**
```bash
docker compose down
```

## 🧾 Example

```
🚀 Starting AI Paris Travel Chatbot...
💬 Interactive Mode: Ask your own Paris-related question!
Type 'exit' to quit.

You: Where is the Arc de Triomphe?
AI: The Arc de Triomphe stands at Place Charles de Gaulle, at the western end of the Champs-Élysées.
```

## 🪪 License

MIT

## 👤 Author & Contact

Olalemi John Oluwatosin
📧 johnnysnipes90@gmail.com

🔗 LinkedIn:
https://www.linkedin.com/in/john-olalemi

🔗 GitHub:
https://github.com/Johnnysnipes90