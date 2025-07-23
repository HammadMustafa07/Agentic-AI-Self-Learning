from agents import (
    Agent,
    AsyncOpenAI,
    Runner,
    OpenAIChatCompletionsModel,
    RunConfig,
    set_tracing_disabled,
    function_tool,
)
import os
from dotenv import load_dotenv
import chainlit as cl

load_dotenv()
set_tracing_disabled(disabled=True)

gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_URL")

external_client = AsyncOpenAI(api_key=gemini_api_key, base_url=gemini_base_url)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

@function_tool
def add(a: int, b: int) -> str:
    """Calculates and returns the sum of two integers as a readable string."""
    return f"{a} + {b} = {a + b}"

agent = Agent(
    name="Math Assistant",
    instructions="You are a smart and friendly math assistant. Use the available tools to answer math-related questions accurately and clearly.",
    model=model,
    tools=[add],
)

@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message("👋 Hi! I'm your Math Assistant. Ask me any math question, like `What is 8 + 12?`").send()

@cl.on_message
async def handle_chat(msg: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role": "user", "content": msg.content})
    result = await Runner.run(agent, input=history)
    history.append({"role": "assistant", "content": result.final_output})
    cl.user_session.set("history", history)

    await cl.Message(content=result.final_output).send()
