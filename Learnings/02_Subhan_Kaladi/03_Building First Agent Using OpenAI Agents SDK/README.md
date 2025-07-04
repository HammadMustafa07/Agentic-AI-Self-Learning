
---

## 📄 Agent Built Using OpenAI Agents SDK and Gemini API

### 🧠 **Overview**

This code defines an intelligent agent named `"Frontend Expert"` using the OpenAI Agents SDK. The agent is connected to **Google Gemini** using an **OpenAI-compatible endpoint** provided by Google.

---

## 📦 Imports

```python
from agents import Runner, Agent, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig
```

* `Runner`: Executes the agent with a given input and configuration.
* `Agent`: The actual AI assistant, defined with a name and behavior.
* `OpenAIChatCompletionsModel`: Wraps a chat model that uses the OpenAI-style API (like GPT or Gemini-compatible).
* `AsyncOpenAI`: Client used to call external OpenAI-style API endpoints (Gemini in this case).
* `RunConfig`: Defines how the agent will run — what model, what provider, etc.

---

```python
import os
from dotenv import load_dotenv
```

* `os`: Used to access environment variables like your Gemini API key.
* `load_dotenv()`: Loads the `.env` file so that you can use your Gemini key securely without hardcoding it.

---

## 🔐 Load API Key

```python
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
```

* Loads environment variables.
* Retrieves your Gemini API key from `.env` using the variable name `GEMINI_API_KEY`.

---

## 🌐 Define External Gemini Client

```python
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
```

* Creates a client (`external_client`) to send API requests.
* Gemini is being accessed via Google’s **OpenAI-compatible** endpoint.
* `AsyncOpenAI` is used to talk to this endpoint using OpenAI-style requests.

> ✅ This endpoint works because Google added OpenAI compatibility for developers.

---

## 🧠 Define Model

```python
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)
```

* Wraps the Gemini model `"gemini-2.0-flash"` in an OpenAI-compatible wrapper.
* Connects it to the external Gemini client created earlier.

---

## ⚙️ Create Agent Run Configuration

```python
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)
```

* `model`: Tells the agent which model to use (Gemini here).
* `model_provider`: Gemini client that will send and receive requests.
* `tracing_disabled=True`: Turns off debugging/tracing logs for now. Set `False` to debug agent reasoning.

---

## 🤖 Create Agent

```python
agent = Agent(
    name="Frontend Expert",
    instructions="You are a frontend expert",
)
```

* Defines your agent with:

  * `name`: Used in tracing/logging/debugging.
  * `instructions`: Tells the model how to behave. In this case, it should act like a **frontend development expert**.

---

## 🏃 Run the Agent

```python
result = Runner.run_sync( 
    agent,
    input="Hello, how are you",
    run_config=config,
)
```

* `Runner.run_sync`: Runs the agent in a blocking (synchronous) way.
* `agent`: The agent you defined earlier.
* `input`: The user message or prompt being sent to the agent.
* `run_config`: The settings (which model to use, how to trace, etc.).

---

## 📤 Print Agent Output

```python
print(result.final_output)
```

* Displays the **final response** from the agent — a friendly and helpful message based on the prompt and the agent’s role as a frontend expert.

---

## ✅ Example Output

```text
I am doing well, thank you for asking! How can I help you with your frontend development needs today?
```

---

## 🧪 Optional: Print Full Run Info for Debugging

To inspect the full response including metadata (model used, steps taken, tools used, etc.), change the last line to:

```python
print(result)
```

---

## 🔚 Summary

| Component                    | Role                                    |
| ---------------------------- | --------------------------------------- |
| `.env` + `load_dotenv()`     | Securely loads API key                  |
| `AsyncOpenAI`                | Talks to Gemini via compatible endpoint |
| `OpenAIChatCompletionsModel` | Wraps the Gemini model in OpenAI format |
| `Agent`                      | Defines AI's identity and role          |
| `RunConfig`                  | Configures model, provider, tracing     |
| `Runner.run_sync`            | Runs the conversation and gets a result |

---

