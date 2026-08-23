from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from backend.app.database.connection import SessionLocal
from backend.app.database.init_db import init_db
from backend.app.database.seed import seed_database

from backend.app.models.ticket import Ticket
from backend.app.models.prediction import Prediction

from backend.app.llm.ticket_agent import classify_ticket
from backend.app.evaluation.reward import calculate_reward


app = FastAPI(
    title="Enterprise Workflow RL Environment",
    description="B2B customer-support workflow and evaluation system",
    version="1.0.0",
)


# ==========================================================
# DATABASE INITIALIZATION
# ==========================================================

@app.on_event("startup")
def startup():

    init_db()


# ==========================================================
# CORS
# ==========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://enterprise-workflow-rl.onrender.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================================
# ROOT
# ==========================================================

@app.get("/")
def root():

    return {
        "message": "Enterprise Workflow RL Environment API",
        "status": "running",
    }


# ==========================================================
# HEALTH
# ==========================================================

@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "service": "enterprise-workflow-api",
    }


# ==========================================================
# SEED DATABASE
# ==========================================================

@app.post("/seed")
def seed():

    try:

        result = seed_database()

        return {
            "message": "Database seed operation completed",
            **result,
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# ==========================================================
# GET TICKETS
# ==========================================================

@app.get("/tickets")
def get_tickets():

    db = SessionLocal()

    try:

        tickets = db.query(Ticket).all()

        return [
            {
                "id": ticket.id,
                "category": ticket.category,
                "customer_tier": ticket.customer_tier,
                "urgency": ticket.urgency,
                "expected_escalation": ticket.expected_escalation,
            }
            for ticket in tickets
        ]

    finally:

        db.close()


# ==========================================================
# PROCESS TICKET
# ==========================================================

@app.post("/tickets/{ticket_id}/process")
def process_ticket(ticket_id: int):

    db = SessionLocal()

    try:

        ticket = (
            db.query(Ticket)
            .filter(Ticket.id == ticket_id)
            .first()
        )

        if not ticket:

            raise HTTPException(
                status_code=404,
                detail="Ticket not found",
            )

        # AI classification
        result = classify_ticket(ticket)

        # Calculate reward
        reward = calculate_reward(
            predicted_escalation=result["escalation"],
            expected_escalation=ticket.expected_escalation,
        )

        # Store prediction
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

        db.refresh(prediction)

        return {
            "ticket_id": ticket.id,
            "customer_message": ticket.customer_message,
            "expected_escalation": ticket.expected_escalation,
            "predicted_category": result["category"],
            "predicted_urgency": result["urgency"],
            "predicted_escalation": result["escalation"],
            "response": result["response"],
            "reward": reward,
            "prediction_id": prediction.id,
        }

    finally:

        db.close()


# ==========================================================
# GET PREDICTIONS
# ==========================================================

@app.get("/predictions")
def get_predictions():

    db = SessionLocal()

    try:

        predictions = db.query(Prediction).all()

        return [
            {
                "id": prediction.id,
                "ticket_id": prediction.ticket_id,
                "predicted_category": prediction.predicted_category,
                "predicted_urgency": prediction.predicted_urgency,
                "predicted_escalation": prediction.predicted_escalation,
                "reward": prediction.reward,
            }
            for prediction in predictions
        ]

    finally:

        db.close()


# ==========================================================
# METRICS
# ==========================================================

@app.get("/metrics")
def get_metrics():

    db = SessionLocal()

    try:

        predictions = db.query(Prediction).all()

        total_predictions = len(predictions)

        if total_predictions == 0:

            return {
                "total_predictions": 0,
                "correct_predictions": 0,
                "accuracy": 0.0,
                "average_reward": 0.0,
            }

        correct_predictions = sum(
            1
            for prediction in predictions
            if prediction.reward == 1
        )

        average_reward = (
            sum(
                prediction.reward
                for prediction in predictions
            )
            / total_predictions
        )

        accuracy = (
            correct_predictions
            / total_predictions
        )

        return {
            "total_predictions": total_predictions,
            "correct_predictions": correct_predictions,
            "accuracy": accuracy,
            "average_reward": average_reward,
        }

    finally:

        db.close()