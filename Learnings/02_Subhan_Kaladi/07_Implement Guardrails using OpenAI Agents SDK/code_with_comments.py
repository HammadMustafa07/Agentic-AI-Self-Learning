# from agents import (
#     Agent,
#     GuardrailFunctionOutput,
#     OutputGuardrailTripwireTriggered,
#     RunContextWrapper,
#     Runner,
#     TResponseInputItem,
#     input_guardrail,
#     output_guardrail,
#     set_tracing_disabled,
#     AsyncOpenAI,
#     OpenAIChatCompletionsModel,
#     InputGuardrailTripwireTriggered,
# ) # from line 1 to line 161

# # ✅ FIXED: os was being imported on the same line as other imports
# import os
# from dotenv import load_dotenv
# from pydantic import BaseModel 
# import chainlit as cl

# # ✅ FIXED: These were on the same line before (invalid Python syntax)
# load_dotenv()
# set_tracing_disabled(disabled=True)

# # 🌐 Load Gemini credentials from environment
# gemini_api_key = os.getenv("GEMINI_API_KEY")
# gemini_base_url = os.getenv("GEMINI_BASE_URL")

# # 🧾 Response model for input guardrail
# class PythonRelatedOutput(BaseModel):
#     is_python_related: bool
#     reasoning: str

# # ✅ FIXED: Using Gemini-compatible client with OpenAI wrapper
# client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url=gemini_base_url
# )

# model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash",
#     openai_client=client
# )

# # ✅ FIXED: Agent definition was correct here
# input_guardrail_agent = Agent(
#     name="Input Guardrail",
#     instructions="Check if the user's question is related to Python programming. Only return true if it is about Python.",
#     output_type=PythonRelatedOutput,
#     model=model
# )

# # ✅ FIXED: Guardrail decorated function was written fine
# @input_guardrail
# async def python_guardrail(
#     ctx: RunContextWrapper[None],
#     agent: Agent,
#     input: str | list[TResponseInputItem]
# ) -> GuardrailFunctionOutput:
#     result = await Runner.run(input_guardrail_agent, input)

#     return GuardrailFunctionOutput(
#         output_info=result.final_output,
#         tripwire_triggered=not result.final_output.is_python_related,
#     )

# # 🧾 Output model for final response
# class MessageOutput(BaseModel):
#     response: str

# class PythonOutput(BaseModel):
#     reasoning: str
#     is_python: bool

# # ✅ FIXED: Previously missing `model=model`, which would crash the agent run
# output_guardrail_agent = Agent(
#     name="Output Guardrail",
#     instructions="Check if the output includes any Python-related response.",
#     output_type=PythonOutput,
#     model=model  # ✅ added this
# )

# @output_guardrail
# async def output_python_guardrail(
#     ctx: RunContextWrapper,
#     agent: Agent,
#     output: str  # ✅ FIXED: It was MessageOutput before, but output is actually a string
# ) -> GuardrailFunctionOutput:
#     # ✅ FIXED: Removed `.response` — because output is already a string
#     result = await Runner.run(output_guardrail_agent, output)

#     return GuardrailFunctionOutput(
#         output_info=result.final_output,
#         tripwire_triggered= not result.final_output.is_python,
#     )

# # ✅ FIXED: Proper agent setup with guardrails
# one_agent = Agent(
#     name="PythonExpert",
#     instructions = "You are an expert Python developer. Only answer questions that are directly related to Python programming. If a question is not about Python, do not provide a response.",
#     model=model,
#     input_guardrails=[python_guardrail],
#     output_guardrails=[output_python_guardrail]
# )

# # 💬 On Chainlit chat start
# @cl.on_chat_start
# async def start():
#     await cl.Message(content="👋 I’m a Python Expert Assistant. Ask me anything about Python programming!").send()

# # 💬 On user message
# @cl.on_message
# async def main(message: cl.Message):
#     try:
#         result = await Runner.run(
#             one_agent,
#             input=message.content
#         )
#         # ✅ FIXED: Previously used final_output directly, should access `.response`
#         await cl.Message(content=result.final_output).send()

#     except InputGuardrailTripwireTriggered:
#         await cl.Message(content="⚠️ Sorry, I can only help with Python programming questions.").send()

#     except OutputGuardrailTripwireTriggered:
#         await cl.Message(content="⚠️ Output blocked due to Python-only policy.").send()
