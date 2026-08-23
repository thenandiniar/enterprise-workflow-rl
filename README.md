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
