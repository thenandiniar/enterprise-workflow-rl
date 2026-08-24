# 🚀 Enterprise Workflow RL Environment

### AI-Powered Enterprise Customer Support Routing & Evaluation System

<p align="center">

AI-driven B2B customer-support workflow that classifies tickets, predicts urgency, routes issues to specialized teams, generates responses, and evaluates decisions using reward-based reinforcement learning concepts.

</p>

<p align="center">

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/FastAPI-API-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
<img src="https://img.shields.io/badge/PostgreSQL-Database-336791?style=for-the-badge&logo=postgresql&logoColor=white" />
<img src="https://img.shields.io/badge/Google-Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white" />
<img src="https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react&logoColor=black" />
<img src="https://img.shields.io/badge/Docker-Containerization-2496ED?style=for-the-badge&logo=docker&logoColor=white" />

</p>



🚀 **Live Demo:** https://enterprise-workflow-rl-1.onrender.com/

An enterprise customer-support workflow and evaluation system powered by AI.

---

# 📌 Overview

**Enterprise Workflow RL Environment** is an end-to-end AI-powered B2B customer-support workflow system.

The application simulates an enterprise support environment where incoming customer tickets are analyzed by an LLM, classified into relevant categories, assigned an urgency level, routed to the correct escalation team, and evaluated using a reward-based system.

The project combines:

- Large Language Models
- Reinforcement Learning concepts
- REST APIs
- PostgreSQL
- React
- Docker
- Automated evaluation

into a single enterprise workflow.

---

# ✨ Features

### 🤖 AI-Powered Ticket Classification

Uses **Google Gemini** to analyze incoming customer-support tickets and determine:

- Ticket category
- Ticket urgency
- Escalation team
- Customer-facing response

### 🎯 Intelligent Ticket Routing

Automatically routes tickets to specialized teams such as:

```text
billing_team
identity_team
technical_team
🚨 Urgency Detection

Tickets are evaluated based on urgency levels such as:

low
medium
high
critical
💬 Automated Response Generation

Gemini generates a customer-facing response based on the ticket context, category, urgency, and escalation decision.

🧠 Reinforcement Learning Environment

Models customer-support routing as a reinforcement-learning-style workflow:

State
  ↓
Action
  ↓
Environment
  ↓
Reward
🏆 Reward-Based Evaluation

Correct escalation decisions receive:

Reward = 1

Incorrect decisions receive:

Reward = 0
🗄️ PostgreSQL Persistence

Stores:

Support tickets
AI predictions
Expected escalation
Predicted escalation
Rewards
Evaluation results
⚡ FastAPI Backend

Provides REST APIs for:

Tickets
Predictions
Processing
Health checks
Evaluation metrics
📊 React Dashboard

Provides a visual interface for monitoring:

Total tickets
Predictions
Accuracy
Average reward
AI routing decisions
Ticket dataset
🐳 Dockerized Infrastructure

PostgreSQL runs through Docker Compose for consistent local development.

🛠️ Tech Stack
Backend
Technology	Purpose
Python	Core programming language
FastAPI	REST API backend
SQLAlchemy	Database ORM
PostgreSQL	Persistent database
Google Gemini	LLM-based ticket analysis
Gymnasium	Reinforcement learning environment
Pydantic	Data validation
Frontend
Technology	Purpose
React	Frontend UI
Vite	Frontend build tool
Axios	API communication
CSS	Dashboard styling
Infrastructure & Tools
Technology	Purpose
Docker	Containerization
Docker Compose	Local infrastructure
Git	Version control
GitHub	Source-code hosting
🧠 System Workflow
                 CUSTOMER SUPPORT TICKET
                           │
                           ▼
                  ┌─────────────────┐
                  │    PostgreSQL   │
                  │  Ticket Dataset │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │     FastAPI     │
                  │    REST API     │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  Google Gemini  │
                  │   LLM Analysis  │
                  └────────┬────────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
          Category      Urgency     Escalation
              │            │            │
              └────────────┼────────────┘
                           ▼
                  ┌─────────────────┐
                  │ Reward System   │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │   PostgreSQL    │
                  │    Results      │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ React Dashboard │
                  └─────────────────┘
🧠 Reinforcement Learning Formulation

The customer-support workflow can be represented as an RL environment.

State

The state contains information about the incoming ticket, such as:

Category
Customer Tier
Urgency
Customer Message
Action

The agent makes a routing decision:

billing_team
identity_team
technical_team
Reward

The routing decision is compared against the expected escalation.

Correct Decision
       ↓
Reward = 1
Incorrect Decision
       ↓
Reward = 0

This provides an evaluation signal for the workflow.

🤖 Google Gemini Integration

Google Gemini acts as the AI reasoning layer of the system.

For example, a ticket such as:

"The verification code is not arriving."

can produce:

{
  "category": "login",
  "urgency": "critical",
  "escalation": "identity_team",
  "response": "We understand the urgency of not receiving your verification code..."
}

The predicted escalation is then compared with the expected escalation stored in the dataset.

📊 Evaluation Metrics

The system exposes an evaluation endpoint:

GET /metrics

Current local evaluation:

Metric	Result
🎫 Total Tickets	100
🤖 Predictions	20
✅ Correct Predictions	20
📈 Accuracy	100%
🏆 Average Reward	1.00
Important Note

The current 100% accuracy represents the 20 stored predictions that were evaluated.

It does not mean all 100 tickets have been processed through Gemini.

🏗️ System Architecture
                         ┌──────────────────────┐
                         │    React Frontend    │
                         │      Dashboard       │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │       FastAPI        │
                         │      REST API        │
                         └──────────┬───────────┘
                                    │
                  ┌─────────────────┴─────────────────┐
                  │                                   │
                  ▼                                   ▼
        ┌──────────────────┐               ┌──────────────────┐
        │    PostgreSQL    │               │   Google Gemini  │
        │                  │               │                  │
        │ • Tickets        │               │ • Classification │
        │ • Predictions    │               │ • Urgency        │
        │ • Rewards        │               │ • Escalation     │
        └────────▲─────────┘               │ • Response       │
                 │                         └─────────┬────────┘
                 │                                   │
                 │                                   ▼
                 │                         ┌─────────────────┐
                 └─────────────────────────│ Reward System   │
                                           └────────┬────────┘
                                                    │
                                                    ▼
                                           ┌─────────────────┐
                                           │ RL Environment  │
                                           └─────────────────┘
📁 Project Structure
enterprise-workflow-rl/
│
├── backend/
│   └── app/
│       │
│       ├── database/
│       │   ├── base.py
│       │   ├── connection.py
│       │   └── init_db.py
│       │
│       ├── evaluation/
│       │   ├── reward.py
│       │   ├── run_evaluation.py
│       │   └── test_reward.py
│       │
│       ├── llm/
│       │   ├── gemini_client.py
│       │   ├── ticket_agent.py
│       │   └── test files
│       │
│       ├── models/
│       │   ├── ticket.py
│       │   └── prediction.py
│       │
│       ├── rl/
│       │   ├── environment.py
│       │   └── test files
│       │
│       ├── services/
│       │   ├── generate_data.py
│       │   └── ticket_generator.py
│       │
│       └── main.py
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
🔌 API

The FastAPI backend provides the following endpoints:

Method	Endpoint	Description
GET	/	API status
GET	/health	Health check
GET	/tickets	Retrieve support tickets
POST	/tickets/{ticket_id}/process	Process a ticket using Gemini
GET	/predictions	Retrieve stored predictions
GET	/metrics	Retrieve evaluation metrics
📖 API Documentation

Once the backend is running:

Swagger UI
http://127.0.0.1:8000/docs
OpenAPI Specification
http://127.0.0.1:8000/openapi.json
⚙️ Setup
1. Clone the Repository
git clone https://github.com/thenandiniar/enterprise-workflow-rl.git
cd enterprise-workflow-rl
2. Create Environment Variables

Create a .env file in the project root:

POSTGRES_DB=enterprise_workflow
POSTGRES_USER=workflow_user
POSTGRES_PASSWORD=your_database_password
POSTGRES_PORT=5432

GEMINI_API_KEY=your_gemini_api_key

⚠️ Never commit .env or API keys to GitHub.

Use .env.example as the public template.

🐳 Start PostgreSQL

From the project root:

docker compose up -d

Check the running container:

docker ps
🌐 Start the Backend

From the project root:

python -m uvicorn backend.app.main:app --reload

Backend:

http://127.0.0.1:8000

Swagger documentation:

http://127.0.0.1:8000/docs
💻 Start the Frontend

Open a new terminal:

cd frontend
npm install
npm run dev

Frontend:

http://localhost:5173
📊 Dashboard

The React dashboard provides a visual overview of the workflow.

Dashboard Metrics
🎫 Total Tickets
🤖 Predictions
📈 Accuracy
🏆 Average Reward
Prediction Monitoring

The dashboard displays:

Prediction ID
Ticket ID
Predicted category
Predicted urgency
Escalation team
Reward
Ticket Dataset

The dashboard also displays the synthetic enterprise ticket dataset, including:

Ticket ID
Category
Customer tier
Urgency
Expected escalation
🗄️ Database

PostgreSQL stores the workflow state and evaluation results.

Main Tables
tickets
predictions
Tickets

Stores:

Customer message
Category
Customer tier
Urgency
Expected escalation
Predictions

Stores:

Ticket ID
Predicted category
Predicted urgency
Predicted escalation
Reward
🔒 Security

Sensitive credentials are managed using environment variables.

The following files are excluded from version control:

.env
.venv/
.venv-1/
node_modules/
__pycache__/

API keys should never be committed to the repository.

🚀 Deployment

The intended production architecture is:

                    Internet
                       │
                       ▼
             ┌──────────────────┐
             │  React Frontend  │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │  FastAPI Backend │
             └────────┬─────────┘
                      │
             ┌────────┴────────┐
             ▼                 ▼
      ┌──────────────┐   ┌──────────────┐
      │  PostgreSQL  │   │ Gemini API   │
      │   Database   │   │              │
      └──────────────┘   └──────────────┘
🔮 Future Improvements
 Process all 100 tickets automatically
 Asynchronous ticket processing
 Authentication and authorization
 Real-time ticket processing
 Advanced evaluation metrics
 Model comparison
 Human feedback loop
 Ticket search and filtering
 Reward visualizations
 Accuracy visualizations
 Production monitoring
 CI/CD pipeline
 Cloud deployment
 Automated evaluation pipeline
🎯 Project Goals

The project demonstrates how multiple production technologies can be combined into an AI-driven enterprise workflow:

LLM
 │
 ▼
AI Decision Making
 │
 ▼
Reward Evaluation
 │
 ▼
Reinforcement Learning Concepts
 │
 ▼
REST API
 │
 ▼
Database
 │
 ▼
React Dashboard
 │
 ▼
Docker
 │
 ▼
Cloud Deployment

Rather than building only a standalone machine-learning model, this project focuses on building an end-to-end AI workflow system.

👩‍💻 Author
Nandini A R

B.Tech — Artificial Intelligence & Machine Learning

GitHub: @thenandiniar

📜 License

This project is intended for educational, portfolio, and experimental purposes.

<p align="center">

⭐ If you find this project interesting, consider giving it a star!

</p> ```
