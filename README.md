# 🗼 AI Paris Travel Chatbot

An **AI-powered virtual tour guide** built with the **OpenAI API**, providing smart, engaging, and informative responses to common Paris travel questions.  
Developed as part of **Peterman Reality Tours’ AI Innovation Series**.

## 🚀 Features

- ✅ Uses **GPT-4o-mini** (configurable) for efficient answers
- ✅ Preloaded with sample questions about Paris landmarks
- ✅ Fully **interactive CLI chat**
- ✅ Saves conversations to JSON for analysis
- ✅ Uses **Rich** for a clean terminal UI
- ✅ Graceful error handling and logging
- ✅ Standard, GitHub-ready structure

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

## 🧑‍💻 Setup

1) **Create and activate a virtual environment**

```bash
# macOS/Linux
python3 -m venv .venv && source .venv/bin/activate

# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2) **Install dependencies**
```bash
pip install -r requirements.txt
```

3) **Set your OpenAI API key**
```bash
# macOS/Linux
export OPENAI_API_KEY="your_api_key_here"

# Windows (PowerShell)
setx OPENAI_API_KEY "your_api_key_here"
$env:OPENAI_API_KEY="your_api_key_here"
```

(Optional) Create a `.env` file with `OPENAI_API_KEY=...`.

4) **Run**
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