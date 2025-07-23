from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled, function_tool
import os
import requests
from dotenv import load_dotenv
import chainlit as cl

# Load environment variables
load_dotenv()
set_tracing_disabled(disabled=True)

# API keys from .env
gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_URL")


# Set up Gemini external client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url=gemini_base_url
)

# Set model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# 🛠️ Weather Tool
@function_tool
def get_weather(city: str) -> str:
    """Fetch current weather data for a given city."""
    try:
        response = requests.get(
            f"http://api.weatherapi.com/v1/current.json?key=8e3aca2b91dc4342a1162608252604&q={city}"
        )
        response.raise_for_status()
        data = response.json()
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        return f"🌤️ The current weather in {city} is {temp}°C with {condition}."
    except Exception as e:
        return f"⚠️ Could not fetch weather data due to: {str(e)} - Response: {response.text if 'response' in locals() else 'No response'}"

# 🧮 Math Tool
@function_tool
def add(a: int, b: int) -> str:
    """Calculates and returns the sum of two integers as a readable string."""
    return f"{a} + {b} = {a + b}"

# 🧠 Create Agent
agent = Agent(
    name="Assistant",
    instructions="You're a helpful assistant that can do math and tell weather updates.",
    tools=[add, get_weather],
    model=model
)

# 🔄 On Chat Start
@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message("👋 Hi! I'm your Assistant. Ask me a math question or a weather update (e.g., `What is 9 + 5?`, `Weather in Lahore`).").send()

# 💬 On Message
@cl.on_message
async def handle_chat(msg: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role": "user", "content": msg.content})

    result = await Runner.run(agent, input=history)

    history.append({"role": "assistant", "content": result.final_output})
    cl.user_session.set("history", history)

    await cl.Message(content=result.final_output).send()
