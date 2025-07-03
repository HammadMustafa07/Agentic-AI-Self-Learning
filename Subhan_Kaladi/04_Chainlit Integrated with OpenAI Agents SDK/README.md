
-----

# 🤖 Simple Agent with Chainlit Integration

Welcome to my first **Agentic AI** project\! This repository showcases how to:

  - ✅ Build a **simple AI Agent** using the [OpenAI Agents SDK](https://platform.openai.com/agents)
  - 💬 Integrate it with [Chainlit](https://www.chainlit.io/) to create an interactive UI
  - 🧠 Store **chat history** for the current session only (non-persistent)

-----

## 🚀 Project Overview

This project provides a foundational example of integrating an AI agent with a user-friendly web interface. It leverages the OpenAI Agents SDK to create a basic agent and Chainlit to build an interactive chat UI. A key feature is the implementation of session-based chat history, ensuring that the agent maintains context within a single user session without persisting data across sessions.

-----

## 🛠️ Tech Stack

  - 🧠 **OpenAI Agents SDK**: For building and managing the AI agent.
  - 🌐 **Chainlit**: A Python framework for creating intuitive chat UIs for LLMs and agents.
  - 🧪 **Python**: The core programming language used for development.
  - 🔑 **.env**: For secure management of API keys and environment variables.

-----

## 📁 Project Structure

```
project/
├── main.py               # Main Chainlit application logic with agent and chat handling
├── .env                  # Environment variables, including your API key
├── requirements.txt      # Python package dependencies
└── README.md             # This documentation file
```

-----

## ▶️ Getting Started

Follow these steps to set up and run the project locally:

1.  **Install Dependencies**:
    Navigate to the project directory and install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

2.  **Configure Environment Variables**:
    Create a `.env` file in the root of your project and add your API key. This example assumes you're using a Gemini API key for an OpenAI-compatible endpoint.

    ```env
    GEMINI_API_KEY=your_api_key_here
    ```

    *Note: Replace `your_api_key_here` with your actual API key.*

3.  **Run the Chainlit Application**:
    Execute the Chainlit application from your terminal:

    ```bash
    chainlit run main.py -w
    ```

    The `-w` flag enables watch mode, which will automatically reload the application on code changes.

4.  **Access the UI**:
    Open your web browser and navigate to the following address:
    [http://localhost:8000](https://www.google.com/search?q=http://localhost:8000)

-----

## ✨ Usage and Behavior

Upon launching the application, you will be greeted with a welcome message from the agent. As you interact with the agent by sending messages, the current session's chat history will be automatically stored and utilized to provide contextual responses. Please note that this history is reset with each new session.

-----

## 📌 Important Notes

  * **Non-Persistent Memory**: This agent is designed with **session-based memory only**. Chat history is maintained exclusively for the duration of the current user session and is not saved across restarts or new sessions.
  * **Simplicity Focus**: The agent in this project is intentionally kept simple to demonstrate core integration. It can be further enhanced with advanced features such as external tools, detailed tracing, more complex memory management, and sophisticated agentic behaviors.

-----

## 📚 Key Learnings

This project served as a valuable learning experience, providing insights into:

  * The fundamental process of creating an AI agent using the OpenAI Agents SDK.
  * Effective integration of large language models (like Gemini) via an OpenAI-compatible endpoint.
  * Leveraging Chainlit to rapidly build interactive and user-friendly chat interfaces.
  * Implementing and managing chat history scoped specifically to the current user session.

-----

## 👨‍💻 Author

**Hammad Abro**
Full-Stack Developer | Agentic AI Explorer

-----