def calculate_reward(
    predicted_escalation: str,
    expected_escalation: str,
) -> float:
    """
    Evaluate whether the AI made the correct escalation decision.

    expected_escalation:
        "yes" -> ticket should be escalated
        "no"  -> ticket should not be escalated

    predicted_escalation:
        "billing_team"
        "technical_team"
        "identity_team"
        "no_escalation"
    """

    escalation_teams = {
        "billing_team",
        "technical_team",
        "identity_team",
    }

    predicted_escalation = predicted_escalation.strip().lower()
    expected_escalation = expected_escalation.strip().lower()

    predicted_requires_escalation = (
        predicted_escalation in escalation_teams
    )

    expected_requires_escalation = (
        expected_escalation == "yes"
    )

    if predicted_requires_escalation == expected_requires_escalation:
        return 1.0

    return -1.0