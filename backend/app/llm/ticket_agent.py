import json

from backend.app.llm.gemini_client import ask_gemini


def classify_ticket(ticket):
    prompt = f"""
You are an enterprise customer-support routing agent.

Analyze the following support ticket.

Customer message:
{ticket.customer_message}

Customer tier:
{ticket.customer_tier}

Urgency:
{ticket.urgency}

Category:
{ticket.category}

Choose exactly one escalation route:
- billing_team
- technical_team
- identity_team

Return ONLY valid JSON in this exact format:

{{
    "category": "...",
    "urgency": "...",
    "escalation": "...",
    "response": "..."
}}

Do not include markdown or additional text.
"""

    result = ask_gemini(prompt)

    return json.loads(result)