import random

from backend.app.database.connection import SessionLocal
from backend.app.database.init_db import init_db
from backend.app.models.ticket import Ticket


CATEGORIES = [
    "billing",
    "bug",
    "login",
]

CUSTOMER_TIERS = [
    "standard",
    "premium",
    "enterprise",
]

URGENCY_LEVELS = [
    "low",
    "medium",
    "high",
    "critical",
]


MESSAGES = {
    "billing": [
        "There is an incorrect charge on my invoice.",
        "I need help understanding my latest billing statement.",
        "Our subscription payment failed unexpectedly.",
        "We were charged twice for the same service.",
        "Please help us update our billing information.",
    ],
    "bug": [
        "The dashboard is displaying incorrect information.",
        "The application crashes when I open the reports page.",
        "The search feature is not returning the correct results.",
        "A workflow is failing unexpectedly.",
        "The system is showing an error when processing requests.",
    ],
    "login": [
        "I cannot log into my account.",
        "Our administrator is unable to access the platform.",
        "The password reset link is not working.",
        "Several users are unable to sign in.",
        "Our organization is locked out of the platform.",
    ],
}


def generate_expected_escalation(customer_tier, urgency):

    if urgency == "critical":
        return "yes"

    if urgency == "high" and customer_tier in ["premium", "enterprise"]:
        return "yes"

    if customer_tier == "enterprise" and urgency == "medium":
        return "yes"

    return "no"


def generate_tickets(count=100):

    tickets = []

    for _ in range(count):

        category = random.choice(CATEGORIES)
        customer_tier = random.choice(CUSTOMER_TIERS)
        urgency = random.choice(URGENCY_LEVELS)

        expected_escalation = generate_expected_escalation(
            customer_tier,
            urgency,
        )

        customer_message = random.choice(
            MESSAGES[category]
        )

        ticket = Ticket(
            category=category,
            customer_tier=customer_tier,
            urgency=urgency,
            expected_escalation=expected_escalation,
            customer_message=customer_message,
        )

        tickets.append(ticket)

    return tickets


def seed_database():

    # Make sure database tables exist
    init_db()

    db = SessionLocal()

    try:

        existing_count = db.query(Ticket).count()

        if existing_count > 0:

            print(
                f"Database already contains "
                f"{existing_count} tickets."
            )

            return {
                "status": "already_seeded",
                "tickets": existing_count,
            }

        tickets = generate_tickets(100)

        db.add_all(tickets)

        db.commit()

        print(
            f"Successfully inserted "
            f"{len(tickets)} tickets."
        )

        return {
            "status": "seeded",
            "tickets": len(tickets),
        }

    finally:

        db.close()


if __name__ == "__main__":
    seed_database()