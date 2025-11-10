# ============================================================
# Project: AI Paris Travel Guide Chatbot
# Author: Olalemi John Oluwatosin
# Company: Peterman Reality Tours (Demo Project)
# Description: Intelligent virtual assistant providing
#              tourist information about Paris using OpenAI API.
# ============================================================

import os
import json
import datetime
from openai import OpenAI
from rich.console import Console
from rich.table import Table

# ==========================
# GLOBAL CONFIGURATIONS
# ==========================
from dotenv import load_dotenv
load_dotenv()
#os.getenv("OPENAI_API_KEY")


MODEL_NAME = "gpt-4o-mini"
LOG_FILE_PATH = "../data/conversation_log.json"

console = Console()

# ==========================
# UTILITY FUNCTIONS
# ==========================

def load_api_client():
    """Initialize and return OpenAI client securely using environment variable."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("❌ Missing API Key! Please set the OPENAI_API_KEY environment variable.")
    return OpenAI(api_key=api_key)


def log_conversation(conversation, filename=LOG_FILE_PATH):
    """Save the conversation list into a JSON file for audit and review."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(conversation, f, indent=4, ensure_ascii=False)


def format_output(conversation):
    """Display conversation in a clean table format using rich library."""
    table = Table(title="Paris Travel Chatbot Conversation", show_lines=True)
    table.add_column("Role", style="cyan bold", no_wrap=True)
    table.add_column("Content", style="white")

    for msg in conversation:
        role = msg['role'].capitalize()
        content = msg['content']
        table.add_row(role, content)
    console.print(table)


# ==========================
# MAIN CHATBOT FUNCTION
# ==========================

def paris_travel_chatbot():
    """
    Main function to run the Paris Travel Assistant chatbot.
    Includes both pre-defined and user-input interactions.
    """

    client = load_api_client()

    # Step 1: Initialize system prompt
    conversation = [
        {
            "role": "system",
            "content": (
                "You are an AI-powered Parisian travel assistant. "
                "Provide concise, friendly, and factually accurate answers about Paris landmarks, museums, attractions, and food. "
                "Avoid irrelevant or speculative content."
            )
        }
    ]

    # Step 2: Predefined tourist questions
    questions = [
        "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
        "Where is the Arc de Triomphe?",
        "What are the must-see artworks at the Louvre Museum?"
    ]

    # Step 3: Loop through each question
    for question in questions:
        conversation.append({"role": "user", "content": question})

        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=conversation,
                temperature=0.0,
                max_tokens=100
            )

            assistant_message = response.choices[0].message.content
            conversation.append({"role": "assistant", "content": assistant_message})

        except Exception as e:
            console.print(f"[bold red]API Error:[/bold red] {str(e)}")
            break

    # Step 4: Allow user to interact manually
    console.print("\n[bold yellow]Interactive Mode: Ask your own Paris-related question![/bold yellow]")
    console.print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            console.print("[bold green]Conversation ended.[/bold green]")
            break

        conversation.append({"role": "user", "content": user_input})
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=conversation,
                temperature=0.0,
                max_tokens=100
            )
            answer = response.choices[0].message.content
            conversation.append({"role": "assistant", "content": answer})
            console.print(f"[bold cyan]AI:[/bold cyan] {answer}\n")

        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {str(e)}")

    # Step 5: Save conversation
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conversation.append({"role": "system", "content": f"Conversation ended at {timestamp}"})
    log_conversation(conversation)
    format_output(conversation)


# ==========================
# ENTRY POINT
# ==========================
if __name__ == "__main__":
    console.print("[bold magenta]Starting AI Paris Travel Chatbot...[/bold magenta]")
    paris_travel_chatbot()