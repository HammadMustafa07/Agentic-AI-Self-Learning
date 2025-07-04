
---

# 🤖 AI Agent with OpenAI Agents SDK + Gemini API

Welcome to my first AI Agent built using the **OpenAI Agents SDK** and powered by **Google Gemini API**!
This project marks my journey into **Agentic AI Development** — now upgraded with **streaming responses** for a smoother and more interactive experience.

🔗 **[Live Demo → Web Dev AI Agent Team 07](https://web_dev_ai_agent_team_07)**

---

## 🚀 Features

* 🔧 Built using **OpenAI's Agent SDK**
* 🤖 Connected with **Google Gemini API**
* 🌊 **Streaming enabled** – get real-time response chunks from the AI
* 🧠 Modular structure for easier scalability and integration
* 📦 Environment variables using `.env`
* 💬 Integrated with **Chainlit** for a chat-based interface

---

## 🛠 Tech Stack

* Python 3.10+
* OpenAI Agents SDK
* Gemini API (via REST)
* Chainlit (for chat UI)
* dotenv for env management
* Async architecture with `AsyncOpenAI`

---

## ⚙️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/ai-agent-gemini.git
cd ai-agent-gemini
```

2. **Install dependencies**

```bash
pip install openai-agents python-dotenv chainlit
```

3. **Add your environment variables**

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_BASE_URL=https://your-gemini-endpoint.com
```

4. **Run the Chainlit app**

```bash
chainlit run app.py
```

---

## 📂 Project Structure

```bash
.
├── agents/
│   ├── agent.py           # Agent configuration
│   ├── runner.py          # Runner setup
│   └── ...
├── .env                   # Environment variables
├── app.py                 # Main Chainlit entry point
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## 🧠 What I Learned

* How to create modular agents with OpenAI SDK
* How to connect external models like Gemini using custom clients
* Implemented real-time **streaming** using OpenAI's `ResponseTextDeltaEvent`
* Integrated Chainlit for a fast development chat UI

---

## 📌 Future Improvements

* Add multiple agent tools (search, math, etc.)
* Deploy the app online (e.g., Render or HuggingFace Spaces)
* Add memory support for context retention
* Authentication layer

---

## 🌐 Live Preview

🔗 **Try it here → [Web Dev AI Agent Team 07](https://web_dev_ai_agent_team_07)**

---

