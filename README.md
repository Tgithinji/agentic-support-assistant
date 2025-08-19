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

## 🗂 Project Architecture

```mermaid
flowchart TD
    A[User Ticket] --> B[Supervisor Agent]
    B -->|Classifies as: Technical / Billing / General| C[Worker Agent]
    C -->|Generates Response| D[Final Reply]
    C -->|Optionally queries FAISS DB| E[(Knowledge Base)]

## How It Works (Step by Step)

Input Ticket

A user submits a support ticket (e.g., “Why was I charged twice this month?”).

Supervisor Agent

Reads the ticket.

Classifies it into one of three categories: Technical, Billing, or General.

Passes both the ticket and the classification result to the Worker Agent.

Worker Agent

Based on the assigned category, it generates a helpful, context-aware reply.

Example: For a billing issue, it creates a polite response suggesting a refund or payment check.

Knowledge Base (Optional)

If the system is extended with FAISS, the Worker Agent can query past support articles or FAQs.

This improves accuracy for more complex, knowledge-driven responses.

Final Reply

The Worker Agent returns a clear, ready-to-send message back to the user.