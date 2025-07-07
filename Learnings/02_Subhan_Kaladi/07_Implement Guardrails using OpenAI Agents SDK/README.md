
---


# 🐍💬 Python Expert Assistant

Welcome to the **Python Expert Assistant** — an AI-powered chatbot that strictly answers **Python programming** questions. Powered by the **Agents SDK**, integrated with **Chainlit**, and enhanced with **input/output guardrails** for focused and safe interactions.

---

## 🚀 Features

✅ **Python-Centric Responses**  
Only answers questions related to Python programming.

🛑 **Input Guardrail**  
Blocks non-Python-related queries *before* reaching the AI agent.

🛡️ **Output Guardrail**  
Ensures the AI response is also about Python — otherwise, it's blocked.

🌐 **Chainlit Integration**  
Interactive, web-based chat interface for seamless usage.

🧠 **Gemini Model Integration**  
Uses **Gemini 2.0 Flash** via OpenAI-style client for intelligent and fast responses.

---

## 🧰 Technologies Used

- 🐍 **Python**
- 🤖 **Agents SDK**
- 💬 **Chainlit**
- 📦 **Pydantic**
- 🔐 **python-dotenv**
- 🌟 **Google Gemini API**

---

## ⚙️ Setup Instructions

### 📁 1. Clone the Repository

```bash
git clone <repository_url>
cd <repository_name>
````

### 🧪 2. (Optional) Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

📌 Sample `requirements.txt`:

```
agents
chainlit
openai
pydantic
python-dotenv
```

### 🔐 4. Configure `.env`

Create a `.env` file in the root directory with the following:

```
GEMINI_API_KEY=your_gemini_api_key
GEMINI_BASE_URL=https://your_gemini_base_url
```

Replace with your actual Gemini credentials.

### ▶️ 5. Run the App

```bash
chainlit run main.py -w
```

Then open your browser at the address Chainlit gives you (usually `http://localhost:8000`).

---

## 🧠 How It Works

| Component                 | Description                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------- |
| `input_guardrail_agent`   | Determines if a user question is Python-related.                                                        |
| `python_guardrail`        | Filters inputs using the above agent. Triggers `InputGuardrailTripwireTriggered` if input is off-topic. |
| `output_guardrail_agent`  | Checks if the AI response is still about Python.                                                        |
| `output_python_guardrail` | Triggers `OutputGuardrailTripwireTriggered` if output deviates from Python.                             |
| `one_agent`               | The core assistant (`PythonExpert`) combining both guardrails.                                          |
| `@cl.on_chat_start`       | Shows welcome message when chat starts.                                                                 |
| `@cl.on_message`          | Handles each incoming message and responds or blocks accordingly.                                       |

---

## 💡 Example Usage

✅ **Valid**:

> "How do I reverse a string in Python?"

❌ **Invalid** (Input Blocked):

> "What's the capital of France?"

❌ **Invalid** (Output Blocked):

> Rare edge case where model tries to give an unrelated answer.

---

## ⚠️ Error Handling

* ❗ If input is not Python-related:

  ```
  ⚠️ Sorry, I can only help with Python programming questions.
  ```

* ❗ If output is off-topic:

  ```
  ⚠️ Output blocked due to Python-only policy.
  ```

---

## 👨‍💻 Author

Built with ❤️ by **Hammad** — exploring Agentic AI with guardrails and intelligent assistants.

---

## 📎 Notes

* This project is meant for **local development and experimentation**.
* No deployment or production configuration included.
* A great example of **responsible AI** using input/output boundaries.

---


