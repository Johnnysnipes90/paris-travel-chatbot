![Paris Travel Chatbot Banner](assets/paris_banner.png)

# 🗼 AI Paris Travel Chatbot

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-green.svg)](https://platform.openai.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B.svg)](https://streamlit.io/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Project Type](https://img.shields.io/badge/Type-Portfolio%20Project-orange.svg)](https://github.com/Johnnysnipes90)

An **AI-powered virtual tour guide** built with the **OpenAI API**, designed to deliver smart, engaging, and informative responses about the beautiful city of Paris.  
This project is developed as part of **Peterman Reality Tours’ AI Innovation Series**.

---

# ✨ Key Features

### ✅ Intelligent AI Travel Assistant  
Uses **GPT-4o-mini** to provide accurate answers on Paris landmarks, museums, food, travel routes, and more.

### ✅ Two Interfaces  
- **CLI Application** (Rich-powered terminal UI)  
- **Streamlit Web App** (modern, beautiful, responsive)

### ✅ Complete Engineering Practices  
- Modular codebase  
- Logging of all conversations  
- Secure environment variable handling  
- Docker + Docker Compose support  
- Clean folder structure suitable for professional teams  

---

# 🧰 Project Structure



```
Paris-Travel-Chatbot/
├── src/
│ ├── paris_chatbot.py # CLI chatbot
│ └── paris_chatbot_app.py # Streamlit web app (GUI)
├── data/
│ └── conversation_log.json # Auto-generated logs
├── .env.example
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
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

5) **Run the CLI Chatbot**
```bash
python src/paris_chatbot.py
```

6) **🌐 Run the Streamlit Web App (GUI)**
```bash
streamlit run src/paris_chatbot_app.py
```

You will see a modern Paris-themed chat interface with:
- ✅ Interactive chat bubbles
- ✅ Typing animation
- ✅ Sidebar quick questions
- ✅ Automatic screen-width responsiveness
- ✅ A hero header and modern layout


# **🐳 Docker Setup**

This project includes full Docker and Docker Compose support.

1) **Build the Docker image**
```bash
docker compose build
```

2) **Run the CLI chatbot inside Docker**
```bash
docker compose up paris-chatbot
```

3) **Run Streamlit Web App**
```bash
docker compose up paris-chatbot-web
```

4) **Stop the chatbot container**
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