
---

# 🌦️ Weather 🤖 Agent

This project is a simple AI-powered weather assistant built using the **OpenAI Agents SDK**, **Chainlit**, and external **WeatherAPI**. It demonstrates how to build a tool-using LLM agent that can respond to user messages and fetch live weather data.

---

## 🚀 Features

- 🤖 Chat agent interface using **Chainlit**
- 📡 Real-time weather data from **WeatherAPI**
- 🧰 Function-calling using OpenAI Agents SDK (`@function_tool`)
- 🔐 Environment variable management with `.env`
- 🌐 Works with any OpenAI-compatible LLM API (e.g., OpenAI, OpenRouter, Gemini if OpenAI-compatible)

---

## 🧠 Agent Behavior

The agent supports two main behaviors:

1. **Weather Queries**   Call the `get_weather(city)` function using real-time data from WeatherAPI.



---

## 🛠️ Stack

| Tool / Library         | Purpose                             |
|------------------------|-------------------------------------|
| `agents` (OpenAI SDK)  | Agent creation and tool integration |
| `Chainlit`             | Frontend chat interface             |
| `dotenv`               | Load environment variables          |
| `requests`             | HTTP calls to external APIs         |
| `WeatherAPI.com`       | Real-time weather info              |

---

## 📂 Project Structure

```

weather-agent/
├── main.py           # Main application logic
├── .env              # API keys and environment variables
├── requirements.txt  # Python dependencies
└── README.md         # This file

````

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/weather-agent.git
cd weather-agent
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `.env` File

Create a `.env` file in the root directory and add:

```env
GEMINI_API_KEY=your_api_key_here
GEMINI_BASE_URL=https://your.openai-compatible-url.com/v1
WEATHER_API_KEY=your_weatherapi_key_here
```

### 4. Run the App

```bash
chainlit run main.py
```

---

## 💡 Example Prompt

> "What's the weather in Lahore right now?"
> → 🌤️ The current weather in Lahore is 32°C with Partly Cloudy skies.

---

## 🧱 Future Improvements

* ✅ Add more tools (e.g. jokes, news, reminders)
* 🔒 Input/output guardrails
* 🧪 Tests for tools
* 💬 Multi-turn conversation memory

---

## 📜 License

MIT License – Free to use for personal and commercial purposes.

---

## 🤝 Acknowledgments

* [Chainlit](https://docs.chainlit.io/) for the beautiful frontend
* [WeatherAPI](https://www.weatherapi.com/) for free weather data
* [OpenAI Agents SDK](https://github.com/openai/agents) for powerful LLM tooling

---

## 🌟 Star This Project

If you found this helpful or inspiring, please ⭐ star the repo!


