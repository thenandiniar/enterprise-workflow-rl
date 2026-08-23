from backend.app.database.connection import SessionLocal
from backend.app.services.ticket_generator import generate_ticket


def generate_and_store_tickets(count: int = 100):
    db = SessionLocal()

    try:
        tickets = [generate_ticket() for _ in range(count)]

        db.add_all(tickets)
        db.commit()

        print(f"Successfully generated and stored {count} tickets.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    generate_and_store_tickets(100)