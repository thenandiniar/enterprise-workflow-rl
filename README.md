# Enterprise Workflow RL Environment

AI-powered enterprise customer-support workflow and evaluation system built with **Python, FastAPI, PostgreSQL, Google Gemini, Gymnasium, React, and Docker**.

## 🚀 Overview

This project simulates a B2B customer-support environment where incoming support tickets are analyzed and routed to the appropriate team.

The system:

- Generates synthetic enterprise support tickets
- Stores tickets and predictions in PostgreSQL
- Uses Google Gemini to classify tickets
- Determines ticket urgency
- Selects the appropriate escalation team
- Generates customer responses
- Calculates rewards for routing decisions
- Exposes the workflow through a FastAPI REST API
- Provides a React dashboard for monitoring predictions and metrics

## 🧠 System Workflow

```text
Customer Support Ticket
          ↓
      PostgreSQL
          ↓
        FastAPI
          ↓
      Google Gemini
          ↓
 Ticket Classification
          ↓
 Urgency + Escalation
          ↓
    Reward Evaluation
          ↓
      PostgreSQL
          ↓
    React Dashboard
✨ Features
Synthetic enterprise support-ticket generation
AI-powered ticket classification
Ticket urgency prediction
Automated escalation routing
Customer response generation
Reward-based evaluation
PostgreSQL data persistence
Gymnasium-compatible RL environment
FastAPI REST API
Interactive Swagger API documentation
React monitoring dashboard
Dockerized PostgreSQL
Evaluation metrics
🛠️ Tech Stack
Backend
Python
FastAPI
SQLAlchemy
PostgreSQL
Gymnasium
Google Gemini API
Frontend
React
Vite
Axios
CSS
Infrastructure
Docker
Docker Compose
Git
GitHub
📁 Project Structure
enterprise-workflow-rl/
│
├── backend/
│   └── app/
│       ├── database/
│       ├── evaluation/
│       ├── llm/
│       ├── models/
│       ├── rl/
│       ├── services/
│       └── main.py
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── vite.config.js
│
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
⚙️ Environment Variables

Create a .env file in the project root:

POSTGRES_DB=enterprise_workflow
POSTGRES_USER=workflow_user
POSTGRES_PASSWORD=your_database_password
POSTGRES_PORT=5432

GEMINI_API_KEY=your_gemini_api_key

Never commit .env or API keys to GitHub.

Use .env.example as the public template.

🐳 Start PostgreSQL

From the project root:

docker compose up -d

Check the running container:

docker ps
🗄️ Database

The application uses PostgreSQL to store:

Support tickets
AI predictions
Reward values

Main tables:

tickets
predictions
🤖 Gemini Integration

Google Gemini analyzes support tickets and produces structured workflow decisions.

Example:

{
  "category": "login",
  "urgency": "critical",
  "escalation": "identity_team",
  "response": "..."
}

The predicted escalation is compared with the expected escalation.

Correct routing:

Reward = 1

Incorrect routing:

Reward = 0
🧠 Reinforcement Learning Environment

The project includes a Gymnasium-compatible environment for modeling the ticket-routing workflow.

Ticket State
     ↓
Agent Action
     ↓
Escalation Decision
     ↓
Reward

The reward provides an evaluation signal for the routing decision.

🌐 FastAPI

Start the backend from the project root:

python -m uvicorn backend.app.main:app --reload

Backend:

http://127.0.0.1:8000

Interactive API documentation:

http://127.0.0.1:8000/docs
🔌 API Endpoints
Method	Endpoint	Description
GET	/	API status
GET	/health	Health check
GET	/tickets	Retrieve support tickets
POST	/tickets/{ticket_id}/process	Process a ticket using Gemini
GET	/predictions	Retrieve stored predictions
GET	/metrics	Retrieve evaluation metrics
📊 Current Evaluation

The current local system contains:

100 synthetic tickets
20 stored predictions
20 correct predictions
100% accuracy
Average reward: 1.00

The reported 100% accuracy represents the currently stored 20 predictions. It does not mean all 100 tickets were processed through Gemini.

💻 React Dashboard

Start the frontend:

cd frontend
npm install
npm run dev

Frontend:

http://localhost:5173

The dashboard displays:

Total tickets
Number of predictions
Accuracy
Average reward
AI routing decisions
Ticket dataset
Prediction results
🏗️ System Architecture
                    ┌─────────────────────┐
                    │    React Frontend   │
                    │      Dashboard      │
                    └──────────┬──────────┘
                               │
                               ↓
                    ┌─────────────────────┐
                    │      FastAPI        │
                    │      REST API       │
                    └───────┬───────┬─────┘
                            │       │
                 ┌──────────┘       └──────────┐
                 ↓                             ↓
       ┌──────────────────┐          ┌─────────────────┐
       │   PostgreSQL     │          │  Google Gemini  │
       │                  │          │                 │
       │ Tickets          │          │ Classification  │
       │ Predictions      │          │ Urgency         │
       │ Rewards          │          │ Escalation      │
       └──────────────────┘          └─────────────────┘
                 ↑
                 │
       ┌─────────┴─────────┐
       │  RL Environment   │
       │  Reward System    │
       └───────────────────┘
🔒 Security

Sensitive credentials are stored using environment variables.

The following are excluded from version control:

.env
.venv/
node_modules/
__pycache__/
🚀 Deployment

The application is designed to be deployed as:

React Frontend
       ↓
FastAPI Backend
       ↓
PostgreSQL
       ↓
Google Gemini API
🔮 Future Improvements
Asynchronous ticket processing
Authentication and authorization
Real-time ticket processing
Advanced evaluation metrics
Model comparison
Human feedback
Ticket search and filtering
Reward and accuracy visualizations
Production monitoring
CI/CD pipeline
👩‍💻 Author

Nandini A R

B.Tech — Artificial Intelligence & Machine Learning

GitHub: @thenandiniar

📜 License

This project is intended for educational, portfolio, and experimental purposes.
