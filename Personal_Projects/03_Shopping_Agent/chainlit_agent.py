import os
import re
import requests
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
import chainlit as cl

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("❌ GEMINI_API_KEY is not set in .env file!")

# Initialize Gemini Client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash", openai_client=external_client
)

config = RunConfig(model=model, model_provider=external_client, tracing_disabled=True)


def search_products(keyword: str) -> str:
    try:
        url = "http://localhost:3000/api/getproductsdata"
        response = requests.get(url)
        response.raise_for_status()
        products = response.json()["products"]

        words = re.findall(r"\b\w+\b", keyword.lower())
        stopwords = {
            "the",
            "with",
            "under",
            "above",
            "for",
            "of",
            "and",
            "or",
            "a",
            "an",
            "in",
            "to",
            "below",
            "between",
            "is",
            "best",
            "items",
        }
        keywords = [w for w in words if w not in stopwords]

        filtered = []
        for p in products:
            title = p.get("name", "").lower()
            description = p.get("description", "").lower()
            category = p.get("category", "").lower()
            if not title:
                continue
            if (
                any(kw in title for kw in keywords)
                or any(kw in description for kw in keywords)
                or any(kw in category for kw in keywords)
            ):
                filtered.append(f"- **{p['name']}**\n  {p['description']}\n")

        if filtered:
            return "\n".join(filtered[:5])
        else:
            return "❌ No matching products found."

    except Exception as e:
        return f"❌ API Error: {str(e)}"


def main():
    print("🛒 Welcome to the Shopping Agent!")

    user_question = "I am Looking for some furnitures"

    product_results = search_products(user_question)

    final_prompt = f"""
You are a shopping assistant. The user asked:
"{user_question}"

Here are the matching products I found:
{product_results}

👉 Please ONLY show the products listed above with short remarks if needed. 
Do not add other suggestions.
"""

    agent = Agent(
        name="Shopping Agent",
        instructions="You help users by showing them filtered product lists from the API. Do not suggest other items.",
        model=model,
    )

    result = Runner.run_sync(agent, final_prompt, run_config=config)
    print("\n🤖 Agent Answer:\n", result.final_output)


if __name__ == "__main__":
    main()
