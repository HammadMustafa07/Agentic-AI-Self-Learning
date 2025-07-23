from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig, set_tracing_disabled, AsyncOpenAI
import os
from dotenv import load_dotenv
import chainlit as cl

load_dotenv()
set_tracing_disabled(disabled=True)

gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_URL")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url=gemini_base_url
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

agent = Agent(
    name="Assistant",
    instructions='You are a helpful AI assistant.',
    model=model
)

@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message("Hello, I am an AI Agent").send()

@cl.on_message
async def handle_message(msg: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role": "user", "content": msg.content})

    result = await Runner.run(agent, input=history)

    history.append({"role": "assistant", "content": result.final_output})
    cl.user_session.set("history", history)

    await cl.Message(content=result.final_output).send()
