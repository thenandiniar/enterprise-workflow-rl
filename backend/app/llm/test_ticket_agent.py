from backend.app.database.connection import SessionLocal
from backend.app.models.ticket import Ticket
from backend.app.llm.ticket_agent import classify_ticket


db = SessionLocal()

try:
    ticket = db.query(Ticket).first()

    if not ticket:
        raise RuntimeError("No tickets found in the database.")

    print("Ticket ID:", ticket.id)
    print("Customer message:", ticket.customer_message)
    print("Expected escalation:", ticket.expected_escalation)

    result = classify_ticket(ticket)

    print("\nGemini decision:")
    print(result)

finally:
    db.close()