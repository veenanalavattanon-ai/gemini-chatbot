from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os
import re

load_dotenv()
app = Flask(__name__)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("models/gemini-1.5-flash")
chat_session = model.start_chat(history=[])

# Define confidential/sensitive patterns
CONFIDENTIAL_PATTERNS = [
    r"\b(?:\d{4}[-\s]?){3}\d{4}\b",                   # credit card format
    r"\b(?:\d{3}[-.\s]?){2}\d{4}\b",                   # SSN or similar
    r"\b[\w.-]+@[\w.-]+\.\w{2,4}\b",                   # email
    r"\b(?:https?://)?[\w.-]+\.[a-z]{2,6}\S*\b",       # URL
    r"(api[_\-]?key|secret|token)\s*[:=]\s*['\"]?[\w-]+['\"]?",  # API keys
    r"\b\d{10}\b",                                     # phone numbers
    r"password\s*[:=]\s*['\"]?.+?['\"]?",              # password
]

# Define basic code-related keywords
CODE_KEYWORDS = [
        "python", "code", "program", "function", "reverse", "sort", "loop",
        "bug", "syntax", "error", "debug", "compile", "script", "variable",
        "data", "logic", "algorithm", "string", "list", "array", "object",
        "class", "html", "css", "sql", "flask", "django", "api", "json",
        "dict", "set", "regex", "input", "output"
]

def is_confidential(text):
    for pattern in CONFIDENTIAL_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False

def is_coding_related(text):
    return any(word.lower() in text.lower() for word in CODE_KEYWORDS)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"reply": "Empty message received."})

    if is_confidential(user_message):
        return jsonify({"reply": "❌ You cannot share confidential or personal data like emails, passwords, phone numbers, or API keys."})

    if not is_coding_related(user_message):
        return jsonify({"reply": "🧠 This chatbot is for coding-related queries only. Please ask about programming, debugging, or development topics."})

    try:
        response = chat_session.send_message(user_message)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
