import random

from backend.app.models.ticket import Ticket


CATEGORIES = [
    "billing",
    "bug_report",
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


TICKET_TEMPLATES = {
    "billing": [
        "I was charged twice for my subscription.",
        "My invoice contains an incorrect amount.",
        "I need help updating my billing information.",
        "My payment failed even though my card is valid.",
        "I was charged for a service I cancelled.",
    ],
    "bug_report": [
        "The dashboard crashes when I upload a file.",
        "The application freezes when I open the reports page.",
        "The search feature returns incorrect results.",
        "The export function is not generating a file.",
        "The application shows an unexpected error.",
    ],
    "login": [
        "I cannot log into my account.",
        "My password reset link is not working.",
        "I am locked out after multiple login attempts.",
        "The verification code is not arriving.",
        "Single sign-on is failing for my account.",
    ],
}


ESCALATION_RULES = {
    "billing": "billing_team",
    "bug_report": "technical_team",
    "login": "identity_team",
}


def generate_ticket() -> Ticket:
    category = random.choice(CATEGORIES)
    customer_tier = random.choice(CUSTOMER_TIERS)
    urgency = random.choice(URGENCY_LEVELS)

    customer_message = random.choice(
        TICKET_TEMPLATES[category]
    )

    expected_escalation = ESCALATION_RULES[category]

    return Ticket(
        customer_message=customer_message,
        category=category,
        customer_tier=customer_tier,
        urgency=urgency,
        expected_escalation=expected_escalation,
    )