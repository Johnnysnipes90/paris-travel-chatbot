# 🗼 AI Paris Travel Chatbot

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-green.svg)](https://platform.openai.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Project Type](https://img.shields.io/badge/Type-Portfolio%20Project-orange.svg)](https://github.com/Johnnysnipes90)


An **AI-powered virtual tour guide** built with the **OpenAI API**, providing smart, engaging, and informative responses to common Paris travel questions.  
Developed as part of **Peterman Reality Tours’ AI Innovation Series**.

---

## 🚀 Features

- ✅ Uses **GPT-4o-mini** (configurable) for efficient answers  
- ✅ Preloaded with sample questions about Paris landmarks  
- ✅ Fully **interactive CLI chat**  
- ✅ Saves conversations to JSON for analysis  
- ✅ Uses **Rich** for a clean terminal UI  
- ✅ Graceful error handling and logging  
- ✅ Standard, GitHub-ready structure  

---

## 🧰 Project Structure


```
Paris-Travel-Chatbot/
├── src/
│   └── paris_chatbot.py
├── data/
│   └── conversation_log.json  # created at runtime
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```


## 🧑‍💻 Setup & Run

1) **Clone the Repository**
   ```bash
   git clone https://github.com/Johnnysnipes90/Paris-Travel-Chatbot.git
   cd Paris-Travel-Chatbot


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
```

5) **Run the Chatbot**
```bash
python src/paris_chatbot.py
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