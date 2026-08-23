def calculate_reward(
    predicted_escalation: str,
    expected_escalation: str,
) -> float:
    """Return a positive reward for correct routing."""

    if predicted_escalation == expected_escalation:
        return 1.0

    return -1.0