import numpy as np
import gymnasium as gym
from gymnasium import spaces

from backend.app.database.connection import SessionLocal
from backend.app.models.ticket import Ticket


class TicketWorkflowEnv(gym.Env):
    """RL environment for enterprise support-ticket routing."""

    def __init__(self):
        super().__init__()

        self.observation_space = spaces.MultiDiscrete([3, 3, 4])
        self.action_space = spaces.Discrete(3)

        self.tickets = []
        self.current_ticket = None

    def _encode_state(self, ticket):
        category_map = {
            "billing": 0,
            "bug_report": 1,
            "login": 2,
        }

        tier_map = {
            "standard": 0,
            "premium": 1,
            "enterprise": 2,
        }

        urgency_map = {
            "low": 0,
            "medium": 1,
            "high": 2,
            "critical": 3,
        }

        return np.array(
            [
                category_map[ticket.category],
                tier_map[ticket.customer_tier],
                urgency_map[ticket.urgency],
            ],
            dtype=np.int64,
        )

    def _get_expected_action(self, ticket):
        escalation_map = {
            "billing_team": 0,
            "technical_team": 1,
            "identity_team": 2,
        }

        return escalation_map[ticket.expected_escalation]

    def reset(self, *, seed=None, options=None):
        super().reset(seed=seed)

        db = SessionLocal()

        try:
            self.tickets = db.query(Ticket).all()
        finally:
            db.close()

        if not self.tickets:
            raise RuntimeError("No tickets found in the database.")

        index = self.np_random.integers(len(self.tickets))
        self.current_ticket = self.tickets[index]

        state = self._encode_state(self.current_ticket)

        return state, {}

    def step(self, action):
        expected_action = self._get_expected_action(
            self.current_ticket
        )

        reward = 1.0 if action == expected_action else -1.0

        terminated = True
        truncated = False

        state = self._encode_state(self.current_ticket)

        info = {
            "ticket_id": self.current_ticket.id,
            "expected_action": expected_action,
            "selected_action": action,
        }

        return state, reward, terminated, truncated, info