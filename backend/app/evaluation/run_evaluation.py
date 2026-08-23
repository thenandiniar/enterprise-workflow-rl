import time

from google.genai import errors

from backend.app.database.connection import SessionLocal
from backend.app.models.ticket import Ticket
from backend.app.models.prediction import Prediction
from backend.app.llm.ticket_agent import classify_ticket
from backend.app.evaluation.reward import calculate_reward


REQUEST_DELAY = 13
MAX_RETRIES = 3


def classify_with_retry(ticket):
    for attempt in range(MAX_RETRIES):
        try:
            return classify_ticket(ticket)

        except errors.ClientError as error:
            if error.code != 429:
                raise

            wait_time = 50 * (attempt + 1)

            print(
                f"Rate limit reached. "
                f"Waiting {wait_time} seconds..."
            )

            time.sleep(wait_time)

    raise RuntimeError(
        f"Could not process ticket {ticket.id} "
        "after multiple retries."
    )


def run_evaluation():
    db = SessionLocal()

    try:
        tickets = db.query(Ticket).all()

        processed = 0
        skipped = 0

        for ticket in tickets:

            existing = (
                db.query(Prediction)
                .filter(Prediction.ticket_id == ticket.id)
                .first()
            )

            if existing:
                skipped += 1
                continue

            print(f"Processing ticket {ticket.id}...")

            result = classify_with_retry(ticket)

            predicted_escalation = result["escalation"]

            reward = calculate_reward(
                predicted_escalation=predicted_escalation,
                expected_escalation=ticket.expected_escalation,
            )

            prediction = Prediction(
                ticket_id=ticket.id,
                predicted_category=result["category"],
                predicted_urgency=result["urgency"],
                predicted_escalation=predicted_escalation,
                response=result["response"],
                reward=reward,
            )

            db.add(prediction)
            db.commit()

            processed += 1

            print(
                f"  Gemini: {predicted_escalation} | "
                f"Expected: {ticket.expected_escalation} | "
                f"Reward: {reward}"
            )

            time.sleep(REQUEST_DELAY)

        print("\nEvaluation complete.")
        print(f"Processed: {processed}")
        print(f"Skipped: {skipped}")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    run_evaluation()