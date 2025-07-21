from agents import Agent, RunConfig, Runner
from tools.tools import (
    fetch_api_data_according_product_name,
    fetch_api_data_according_category,
)
import chainlit as cl
from configurations.config import model


agent = Agent(
    name="Data Fetcher Assistant",
    instructions="""  
You are a data-retrieval assistant.  
- Always use the provided API Tools to fetch answers for user queries.  

- Use `fetch_api_data_according_product_name` when the user asks for a product by name (for example, "sunglasses" or "headphones").  

- Use `fetch_api_data_according_category` when the user mentions a category (for example, "fashion", "electronics", "furniture").  

- If the user specifically asks for sunglasses or product data related to something, always use `fetch_api_data_according_product_name` with the query "sunglasses".  

- If the user mentions a category, use the category fetch tool with the category name.  

- If the API returns a 'formatted_output', reply exactly with its content without changing it.  

- Do NOT summarize, bullet-point, or alter the response.  

- If no data is found or there is an error, reply with the message from 'formatted_output'.  

- Never use your own knowledge, guesses, or assumptions.  
""",
    tools=[fetch_api_data_according_product_name, fetch_api_data_according_category],
)


@cl.on_chat_start
async def handle_start_chat():
    cl.user_session.set("history", [])
    await cl.Message(
        "🤖 I'm your Product Finder Agent! 🕵️‍♂️\n\nYou can ask me for products by **category** 📂 or **product name** 🛒 — and I’ll fetch the matching items for you!"
    ).send()


@cl.on_message
async def handle_on_message(msg: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role": "user", "content": msg.content})

    result = await Runner.run(
        agent, input=msg.content, run_config=RunConfig(model=model)
    )

    history.append({"role": "assistant", "content": result.final_output})
    cl.user_session.set("history", history)

    await cl.Message(content=result.final_output).send()
