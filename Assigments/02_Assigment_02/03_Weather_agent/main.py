from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
    function_tool,
    input_guardrail,
    output_guardrail,
    RunContextWrapper,
    TResponseInputItem,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    OutputGuardrailTripwireTriggered
)
from dotenv import load_dotenv
from pydantic import BaseModel
import os
import requests
import chainlit as cl

# Load environment variables
load_dotenv()
set_tracing_disabled(disabled=True)

# Setup Gemini API via OpenRouter (or custom provider)
gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_URL")
weather_api_key = os.getenv("WEATHER_API_KEY")

# ---------------------- Pydantic Output Model ------------------
class WeatherRelatedOutput(BaseModel):
    is_weather_related: bool
    resoning: str

# ---------------------- Model Setup ------------------
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url=gemini_base_url,
)


model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",  # 🔧 RECOMMENDED: use a valid model like "gemini-pro" if "gemini-2.0-flash" causes issues
    openai_client=provider
)

# ---------------------- Input Guardrail Agent ------------------
input_guardrail_agent = Agent(
    name="Input Guardrail Agent",
    instructions="Check if the user's question is related to Weather. Only return true if it is about Weather.",
    output_type=WeatherRelatedOutput,
    model=model,
)

@input_guardrail
async def handle_input_guardrail(
    ctx: RunContextWrapper[None],
    agent: Agent,
    input: str | list[TResponseInputItem],
) -> GuardrailFunctionOutput:
    result = await Runner.run(input_guardrail_agent, input)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_weather_related
    )

# ---------------------- Output Guardrail Agent 🔧 ADDED ------------------
output_guardrail_agent = Agent(
    name="Output Guardrail Agent",
    instructions="Check if the output is related to Weather. Only allow responses that are about weather.",
    output_type=WeatherRelatedOutput,
    model=model,
)

@output_guardrail
async def handle_output_guardrail(
    ctx: RunContextWrapper,
    agent: Agent,
    output: str
) -> GuardrailFunctionOutput:
    result = await Runner.run(output_guardrail_agent, output)  # 🔧 FIXED: used correct agent here
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_weather_related
    )

# -------------------- Tool Functions --------------------
@function_tool
def get_weather(city: str) -> str:
    """Fetch current weather data for a given city."""
    try:
        response = requests.get(
            f"http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={city}"
        )
        data = response.json()
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        return f"🌤️ The current weather in {city} is {temp}°C with {condition}."
    except Exception as e:
        return f"⚠️ Could not fetch weather data due to: {e}"

# -------------------- Main Agent Configuration --------------------
agent = Agent(
    name="🌤️ Weather Agent",
    instructions="""
Respond to the user's request using the appropriate tool:

- If the user asks for jokes:
  1. Call the `how_many_jokes` function.
  2. Generate and return that many numbered jokes.

- If the user asks for weather:
  Call the `get_weather` function with the provided city name.
""",
    model=model,
    input_guardrails=[handle_input_guardrail],
    output_guardrails=[handle_output_guardrail],
    tools=[get_weather]
)

# -------------------- Chainlit Events --------------------
@cl.on_chat_start
async def handle_start_of_chat():
    cl.user_session.set("history", [])
    await cl.Message("👋 Hi! I'm your Weather 🤖 Agent. Ask me something about the weather!").send()

@cl.on_message
async def handle_chat(message: cl.Message):
    try:
        history = cl.user_session.get("history")
        history.append({"role": "user", "content": message.content})

        result = await Runner.run(agent, input=history)

        history.append({"role": "assistant", "content": result.final_output})
        cl.user_session.set("history", history)

        await cl.Message(content=result.final_output).send()

    # 🔧 FIXED: Correct order of exceptions. Specific ones first
    except InputGuardrailTripwireTriggered:
        await cl.Message(content="⚠️ I am only allowed to respond to weather-related queries.").send()

    except OutputGuardrailTripwireTriggered:
        await cl.Message(content="⚠️ My response was not related to weather, so I didn’t send it.").send()

    except Exception as e:
        await cl.Message(content=f"❌ Couldn't fetch the weather. Error: {str(e)}").send()
