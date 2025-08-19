# 🧑‍💻 Multi-Agent Support Ticket Assistant

A simple demonstration of **multi-agent orchestration** using LangChain + OpenAI.

## 🔹 Project Overview
This prototype simulates how **Supervisor–Worker AI agents** can classify and resolve customer support tickets.

- **Supervisor Agent** → classifies incoming tickets (Technical, Billing, General).
- **Worker Agent** → generates responses based on category.
- **Memory** → keeps track of conversation context.
- **Vector DB (planned)** → extend with FAISS for retrieval-augmented responses.

## 🔹 Tech Stack
- Python
- LangChain
- OpenAI API
- FAISS (vector DB)

## 🔹 Example Run
Input Ticket: "I can't log into my account."
Supervisor → Technical
Worker → "Sorry to hear about your login issue. Please try resetting your password..."


## 🔹 Future Enhancements
- Add FAISS for RAG knowledge base
- Connect to real ticketing system via API
- Add multi-turn state monitoring