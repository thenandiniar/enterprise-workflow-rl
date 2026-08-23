from backend.app.database.connection import SessionLocal
from backend.app.models.ticket import Ticket
from backend.app.models.prediction import Prediction
from backend.app.llm.ticket_agent import classify_ticket
from backend.app.evaluation.reward import calculate_reward


db = SessionLocal()

try:
    ticket = db.query(Ticket).first()

    if not ticket:
        raise RuntimeError("No tickets found in the database.")

    print("Ticket ID:", ticket.id)
    print("Expected escalation:", ticket.expected_escalation)

    result = classify_ticket(ticket)

    predicted_escalation = result["escalation"]

    reward = calculate_reward(
        predicted_escalation=predicted_escalation,
        expected_escalation=ticket.expected_escalation,
    )

    prediction = Prediction(
        ticket_id=ticket.id,
        predicted_category=result["category"],
        predicted_urgency=result["urgency"],
        predicted_escalation=result["escalation"],
        response=result["response"],
        reward=reward,
    )

    db.add(prediction)
    db.commit()

    print("Gemini escalation:", predicted_escalation)
    print("Reward:", reward)
    print("Prediction saved successfully.")

except Exception:
    db.rollback()
    raise

finally:
    db.close()