from agents import (
    OpenAIChatCompletionsModel,
    AsyncOpenAI,
    set_tracing_disabled,
)
import os
import logging
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

load_dotenv()
set_tracing_disabled(disabled=True)

gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_URL")

if not gemini_api_key or not gemini_base_url:
    raise EnvironmentError("Gemini API credentials are missing in the environment.")

external_client = AsyncOpenAI(api_key=gemini_api_key, base_url=gemini_base_url)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash", openai_client=external_client
)
