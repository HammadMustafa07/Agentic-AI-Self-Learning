
---

# 🤖 MyShopping Assistant — OpenAI SDK + Gemini API Powered Agent

This project features an AI-powered shopping assistant built with the **OpenAI Python SDK**, capable of intelligently fetching product data from an external API using **function calling** and **agentic behavior**.

Additionally, it supports integration with **Gemini AI API** for multi-model experiments and responses.

---

## 🎯 What Does This Project Offer?

* ✅ OpenAI SDK agent with **function calling** to fetch product data
* ✅ Real-time API integration using Python
* ✅ Gemini AI API support with configurable API Key & Base URL
* ✅ Clean separation of tools, API calling logic, and agent handling

---

## 🛠️ Tech Stack

* **OpenAI Python SDK** — for agents and tool calling
* **Google Gemini API** — optional multi-model integration
* **Python 3.11+**
* **Requests** — to interact with external product APIs
* **Dotenv** — for environment variable handling
* **Logging** — structured logs for debugging


---

## ⚙️ Environment Configuration

Create a `.env` file in the project root with the following keys:

```dotenv
# OpenAI API Key  
OPENAI_API_KEY=your_openai_api_key  

# Gemini API Key (Optional, for Gemini integration)  
GEMINI_API_KEY=your_gemini_api_key  

# Gemini Base URL (default for Gemini Pro)  
GEMINI_BASE_URL=https://generativelanguage.googleapis.com/v1beta  
```

---

## 🚀 How to Run

```bash
pip install openai-agents python-dotenv requests chainlit
python Agent.py  
```

---

## 🗒️ How It Works

1️⃣ User sends a product query (e.g., "Find me wireless headphones")
2️⃣ OpenAI Agent uses **function calling** to hit the Product API
3️⃣ Gemini API can be called (optional) for enhanced AI responses
4️⃣ The agent returns structured results to the user

---

## 💡 Ideal Use Cases

* AI Shopping Assistants
* Chainlit AI Integrations
* API-Calling AI Agents with OpenAI SDK
* Multi-Agent & Multi-Model Prototyping

---

## 🙏 Special Thanks

To my teachers, mentors, and peers who guided me in mastering AI integrations and real-world API interactions.

---

## 📜 License

MIT License

---
