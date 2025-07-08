
---

# 🌤️ Weather Agent with Guardrails (OpenAI Agents SDK + Chainlit)

This project implements a smart weather assistant powered by **OpenAI Agents SDK**, **Gemini via OpenRouter**, **Chainlit**, and **WeatherAPI**. It ensures **safety and relevance** using input and output **guardrails**, restricting the assistant to only process **weather-related** queries.

## 🔍 Overview

The assistant:
- Uses **Pydantic-based guardrails** to filter input and output.
- Integrates with the **WeatherAPI** to provide real-time weather data.
- Uses **Gemini 2.0** via **OpenRouter** as the language model.
- Runs in a **Chainlit UI** for a smooth chat experience.

---

## 🚀 Features

✅ Weather-aware responses  
✅ Guardrails to block irrelevant prompts  
✅ Realtime weather from WeatherAPI  
✅ Friendly Chainlit chat interface  
✅ Tool usage with decorators (e.g., `@function_tool`)  
✅ Gemini model integration via OpenRouter  

---

## 🧠 How It Works

1. **Input Guardrail**: Checks if user’s query is weather-related.  
2. **Main Agent**: Uses the appropriate tool (e.g., `get_weather`) based on the request.  
3. **Output Guardrail**: Ensures the assistant's response is about weather.  
4. **Chainlit Frontend**: Displays the chat session interactively.

---

## 🔧 Environment Setup

### 1. Install Dependencies

```bash
pip install openai_agents requests python-dotenv chainlit
````



```text
openai
python-dotenv
pydantic
requests
chainlit
agents  # from openai-agents-sdk
```

</details>

---

### 2. Create a `.env` file

```env
GEMINI_API_KEY=your_openrouter_key
GEMINI_BASE_URL=https://openrouter.ai/api/v1
WEATHER_API_KEY=your_weatherapi_key
```

---

## 💡 Available Tool

### 🛠️ `get_weather(city: str) -> str`

Fetches the current temperature and weather condition of the given city using WeatherAPI.

---

## 🧪 Sample Queries

```text
❓ What’s the weather in Karachi?
✅ 🌤️ The current weather in Karachi is 34°C with Sunny.

❌ Tell me a joke.
⚠️ I am only allowed to respond to weather-related queries.
```

---

## 🖼️ UI Demo (Chainlit)

When the app runs, Chainlit opens an interactive web chat:

* Start with a friendly message.
* Ask a weather-related question.
* Get real-time results with stickers and emojis.

---

## 🤝 Gratitude

A special shoutout to my teachers and mentors whose guidance made this possible:

* **@Subhan Kaladi**
* **@Hammad Mustafa**
* **Agentic AI Community**

---

## 📂 Project Structure

```
weather_agent/
├── main.py             # Main Chainlit + agent logic
├── .env                # Secrets and API keys
├── requirements.txt    # Python dependencies
└── README.md           # You're reading it!
```

---

## 🔗 References

* [Chainlit Docs](https://docs.chainlit.io/)
* [OpenAI Agents SDK](https://github.com/openai/agents)
* [OpenRouter](https://openrouter.ai/)
* [WeatherAPI](https://www.weatherapi.com/)

---

## 🏁 Run the App

```bash
chainlit run main.py
```

Then open the URL shown (typically `http://localhost:8000`) in your browser.

---