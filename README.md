# 🤖 Gemini Coding Chatbot

A coding-focused chatbot powered by **Google's Gemini AI** and built using **Python Flask**.  
It answers programming-related questions and blocks any messages containing confidential data.  

---

## 🌟 Features

- 💬 Gemini AI integration using Google Generative Language API
- 🔐 Blocks sensitive data (e.g., passwords, tokens, emails)
- 👨‍💻 Focuses only on programming/coding-related queries
- 📱 Responsive, mobile-like chat UI (WhatsApp-inspired)
- 🎨 Dark blue/light blue theme for clean visual experience
- 🐳 Docker support for simple deployment

---

## 📁 Project Structure

gemini-chatbot/
├── app.py # Flask backend
├── templates/
│ └── index.html # Chat UI
├── .env # Gemini API Key (excluded via .gitignore)
├── .gitignore # Ignores unnecessary files and secrets
├── Dockerfile # Docker config
├── LICENSE # Project license
└── README.md # Project documentation


---

## 🚀 Getting Started

### 🔧 Local Setup 

```bash
git clone https://github.com/veenanalavattanon-ai/gemini-chatbot.git
cd gemini-chatbot

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "GOOGLE_API_KEY=your_gemini_api_key" > .env

# Run locally
python app.py

#🐳 Docker Setup

# Build Docker image
docker build -t gemini-chatbot .

# Run container
docker run -p 5000:5000 --env-file .env gemini-chatbot

📌 Note

    This chatbot is intentionally restricted to programming-related queries only.
    Sharing confidential data like credentials, secrets, or personal information is strictly blocked.


