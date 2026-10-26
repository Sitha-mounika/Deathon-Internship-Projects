
import json
import random
import datetime
from pathlib import Path


# Locate the FAQ dataset in the same folder as this program
DATASET_FILE = Path(__file__).parent / "sample_faq.json"


# Load the JSON dataset
def load_dataset():
    try:
        with open(DATASET_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        data.setdefault("greetings", [])
        data.setdefault("faqs", [])
        return data

    except FileNotFoundError:
        print("Error: sample_faq.json was not found.")
        print("Please keep it in the same folder as chatbot.py.")
        return {"greetings": [], "faqs": []}

    except json.JSONDecodeError:
        print("Error: sample_faq.json contains invalid JSON.")
        return {"greetings": [], "faqs": []}


DATA = load_dataset()


# Recognize common greeting variations
def is_greeting(message):
    greeting_variations = {
        "hi", "hii", "hiii", "hiiii",
        "hello", "helloo", "hellooo",
        "hey", "heyy", "heyyy",
        "good morning", "good afternoon", "good evening"
    }

    dataset_greetings = {
        greeting.lower().strip()
        for greeting in DATA["greetings"]
    }

    return message in dataset_greetings or message in greeting_variations


# Identify what the user wants
def recognize_intent(message):
    message = message.lower().strip()

    # Exit commands
    if message in {"bye", "goodbye", "exit", "quit"}:
        return "goodbye"

    # Greeting
    if is_greeting(message):
        return "greeting"

    # Help
    if message in {"help", "menu"} or "what can you do" in message:
        return "help"

    # Time and date
    if "time" in message:
        return "time"

    if "date" in message or "today" in message:
        return "date"

    # Match the FAQ questions from the JSON dataset
    for faq in DATA["faqs"]:
        question = faq.get("question", "").lower().strip()

        if question and (
            message == question
            or message in question
            or question in message
        ):
            return "faq"

    # Common variations for the internship FAQs
    if "hour" in message or "operation" in message or "open" in message:
        return "hours_faq"

    if (
        "submit" in message
        or "submission" in message
        or "github" in message
    ):
        return "submission_faq"

    if "certificate" in message or "certification" in message:
        return "certificate_faq"

    if "python" in message:
        return "python"

    if "study" in message or "learn" in message:
        return "study"

    if "thank" in message:
        return "thanks"

    return "unknown"


# Find an FAQ answer using keywords
def find_faq_answer(intent, message):
    message = message.lower()

    keywords = {
        "hours_faq": ["hours", "operation", "open", "working time"],
        "submission_faq": ["submit", "submission", "github", "project"],
        "certificate_faq": ["certificate", "certification"]
    }

    for faq in DATA["faqs"]:
        question = faq.get("question", "").lower()
        answer = faq.get("answer", "")

        if any(keyword in question for keyword in keywords.get(intent, [])):
            return answer

    return None


# Generate a response
def generate_response(message, intent):
    responses = {
        "greeting": [
            "Hello! Welcome to PyBot.",
            "Hi there! How can I help you?",
            "Hey! Ask me an internship FAQ."
        ],
        "help": [
            "I can answer internship FAQs, tell you the date and time, "
            "and provide basic Python and study tips.\n"
            "Try asking about working hours, project submission, "
            "or your certificate."
        ],
        "python": [
            "Python is a beginner-friendly programming language "
            "used for automation, data analysis, and application development."
        ],
        "study": [
            "Try learning one topic at a time and practising with small projects.",
            "Consistent practice helps you improve your programming skills."
        ],
        "thanks": [
            "You're welcome!",
            "Happy to help!"
        ],
        "goodbye": [
            "Goodbye! Best wishes for your internship projects."
        ],
        "unknown": [
            "Sorry, I didn't understand that.",
            "Please try another question or type 'help' for assistance."
        ]
    }

    if intent == "time":
        return "Current time: " + datetime.datetime.now().strftime("%I:%M:%S %p")

    if intent == "date":
        return "Today's date: " + datetime.datetime.now().strftime("%d-%m-%Y")

    if intent in {
        "faq", "hours_faq", "submission_faq", "certificate_faq"
    }:
        answer = find_faq_answer(intent, message)

        if answer:
            return answer

        if intent == "faq":
            for faq in DATA["faqs"]:
                question = faq.get("question", "").lower().strip()

                if question and (
                    message == question
                    or message in question
                    or question in message
                ):
                    return faq.get("answer", "Sorry, no answer is available.")

        return "Sorry, I couldn't find an answer in the FAQ dataset."

    return random.choice(responses.get(intent, responses["unknown"]))


# Start the chatbot
def run_chatbot():
    print("=" * 50)
    print("       PYBOT - INTERNSHIP FAQ CHATBOT")
    print("=" * 50)
    print("Type 'help' for assistance.")
    print("Type 'bye' to exit.\n")

    if not DATA["faqs"]:
        print("Warning: No FAQs loaded. Check sample_faq.json.\n")

    while True:
        try:
            message = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nPyBot: Goodbye!")
            break

        if not message:
            print("PyBot: Please enter a message.\n")
            continue

        intent = recognize_intent(message)
        response = generate_response(message, intent)

        print("PyBot:", response, "\n")

        if intent == "goodbye":
            break


if __name__ == "__main__":
    run_chatbot()

