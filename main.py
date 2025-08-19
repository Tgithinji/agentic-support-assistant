from agents.supervisor import classify_ticket
from agents.worker import handle_response

def handle_ticket(ticket_text: str):
    category = classify_ticket(ticket_text)
    print(f"Supervisor classified ticket as: {category}")

    reply = handle_response(ticket_text, category)
    print(f"Worker Response:\n{reply}\n")
    return reply

if __name__ == "__main__":
    tickets = [
        "I can't log into my account, the password reset isn't working.",
        "Why was I charged twice this month?",
        "What are your business hours?"
    ]

    for t in tickets:
        handle_ticket(t)
