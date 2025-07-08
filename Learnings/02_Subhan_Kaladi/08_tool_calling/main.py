from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
    function_tool,
)
from dotenv import load_dotenv
import os
import requests
import random
import chainlit as cl

# Load environment variables
load_dotenv()
set_tracing_disabled(disabled=True)

# Setup Gemini API via OpenRouter (or custom provider)
gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_URL")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url=gemini_base_url,
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

# -------------------- Tool Functions --------------------

@function_tool
def how_many_jokes():
    """Generate a random number of jokes to tell."""
    return random.randint(1, 11)

@function_tool
def get_weather(city: str) -> str:
    """Fetch current weather data for a given city."""
    try:
        response = requests.get(
            f"http://api.weatherapi.com/v1/current.json?key=8e3aca2b91dc4342a1162608252604&q={city}"
        )
        data = response.json()
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        return f"🌤️ The current weather in {city} is {temp}°C with {condition}."
    except Exception as e:
        return f"⚠️ Could not fetch weather data due to: {e}"

# -------------------- Agent Configuration --------------------

agent = Agent(
    name="Assistant",
    instructions="""
Respond to the user's request using the appropriate tool:

- If the user asks for jokes:
  1. Call the `how_many_jokes` function.
  2. Generate and return that many numbered jokes.

- If the user asks for weather:
  Call the `get_weather` function with the provided city name.
""",
    model=model,
    tools=[get_weather, how_many_jokes]
)

# -------------------- Chainlit Events --------------------

@cl.on_chat_start
async def handle_start_of_chat():
    cl.user_session.set("history", [])
    await cl.Message("👋 Hi! I'm your Weather 🤖Agent. Ask me something!").send()

@cl.on_message
async def handle_chat(message: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role": "user", "content": message.content})
    
    result = await Runner.run(agent, input=history)
    
    history.append({"role": "assistant", "content": result.final_output})
    cl.user_session.set("history", history)
    
    await cl.Message(content=result.final_output).send()
