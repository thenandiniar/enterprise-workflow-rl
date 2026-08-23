def calculate_reward(
    predicted_escalation: str,
    expected_escalation: str,
) -> float:
    """
    Calculate reward by comparing whether the AI decided
    to escalate with the expected escalation decision.

    Expected escalation:
        "yes" / "no"

    Predicted escalation:
        "billing_team"
        "technical_team"
        "identity_team"
    """

    # Any team route means the AI decided to escalate.
    predicted_should_escalate = predicted_escalation in {
        "billing_team",
        "technical_team",
        "identity_team",
    }

    # Convert database value to boolean.
    expected_should_escalate = expected_escalation.lower() == "yes"

    # Correct routing decision.
    if predicted_should_escalate == expected_should_escalate:
        return 1.0

    # Incorrect routing decision.
    return -1.0