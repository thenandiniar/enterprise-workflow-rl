import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

const API = "https://enterprise-workflow-rl.onrender.com";

function App() {
  const [metrics, setMetrics] = useState(null);
  const [tickets, setTickets] = useState([]);
  const [predictions, setPredictions] = useState([]);
  const [selectedTicket, setSelectedTicket] = useState(null);
  const [selectedPrediction, setSelectedPrediction] = useState(null);
  const [loading, setLoading] = useState(true);
  const [processing, setProcessing] = useState(false);

  async function loadDashboard() {
    try {
      const [metricsRes, ticketsRes, predictionsRes] = await Promise.all([
        axios.get(`${API}/metrics`),
        axios.get(`${API}/tickets`),
        axios.get(`${API}/predictions`),
      ]);

      setMetrics(metricsRes.data);
      setTickets(ticketsRes.data);
      setPredictions(predictionsRes.data);

      if (predictionsRes.data.length > 0) {
        const latest = predictionsRes.data[predictionsRes.data.length - 1];
        setSelectedPrediction(latest);

        const ticket = ticketsRes.data.find(
          (t) => t.id === latest.ticket_id
        );

        if (ticket) {
          setSelectedTicket(ticket);
        }
      }
    } catch (error) {
      console.error("Dashboard loading failed:", error);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadDashboard();
  }, []);

  async function processTicket(ticketId) {
    setProcessing(true);

    try {
      await axios.post(`${API}/tickets/${ticketId}/process`);
      await loadDashboard();
    } catch (error) {
      console.error("Ticket processing failed:", error);

      const message =
        error.response?.data?.detail ||
        "Unable to process ticket.";

      alert(message);
    } finally {
      setProcessing(false);
    }
  }

  function selectTicket(ticket) {
    setSelectedTicket(ticket);

    const prediction = predictions.find(
      (p) => p.ticket_id === ticket.id
    );

    setSelectedPrediction(prediction || null);
  }

  if (loading) {
    return (
      <div className="loading-screen">
        <div className="loader"></div>
        <h2>Loading Enterprise Workflow AI</h2>
        <p>Connecting to the evaluation environment...</p>
      </div>
    );
  }

  return (
    <div className="app">

      {/* ================================================= */}
      {/* HEADER */}
      {/* ================================================= */}

      <header className="topbar">

        <div className="brand">
          <div className="brand-icon">EW</div>

          <div>
            <h1>Enterprise Workflow AI</h1>
            <p>AI-powered support routing & evaluation</p>
          </div>
        </div>

        <div className="system-status">
          <span className="live-dot"></span>
          API ONLINE
        </div>

      </header>


      {/* ================================================= */}
      {/* METRICS */}
      {/* ================================================= */}

      <main className="dashboard">

        <section className="metrics-grid">

          <MetricCard
            label="Total Tickets"
            value={tickets.length}
            description="Synthetic enterprise tickets"
          />

          <MetricCard
            label="Predictions"
            value={metrics?.total_predictions ?? 0}
            description="AI routing decisions"
          />

          <MetricCard
            label="Accuracy"
            value={`${((metrics?.accuracy ?? 0) * 100).toFixed(0)}%`}
            description="Routing correctness"
          />

          <MetricCard
            label="Average Reward"
            value={(metrics?.average_reward ?? 0).toFixed(2)}
            description="Evaluation signal"
          />

        </section>


        {/* ================================================= */}
        {/* WORKFLOW */}
        {/* ================================================= */}

        <section className="workflow-section">

          <div className="section-heading">
            <div>
              <span className="eyebrow">DECISION PIPELINE</span>
              <h2>Enterprise Support Workflow</h2>
              <p>
                Observe how a customer ticket moves through the AI
                routing and evaluation pipeline.
              </p>
            </div>
          </div>


          <div className="workflow">

            <WorkflowNode
              number="01"
              title="Customer Ticket"
              subtitle="Incoming support request"
              icon="🎫"
              active={!!selectedTicket}
            />

            <WorkflowArrow />

            <WorkflowNode
              number="02"
              title="AI Agent"
              subtitle="Gemini classification"
              icon="🤖"
              active={!!selectedPrediction}
            />

            <WorkflowArrow />

            <WorkflowNode
              number="03"
              title="Decision"
              subtitle="Category + urgency"
              icon="🧠"
              active={!!selectedPrediction}
            />

            <WorkflowArrow />

            <WorkflowNode
              number="04"
              title="Escalation"
              subtitle="Workflow routing"
              icon="↗"
              active={!!selectedPrediction}
            />

            <WorkflowArrow />

            <WorkflowNode
              number="05"
              title="Reward"
              subtitle="Evaluation signal"
              icon="★"
              active={!!selectedPrediction}
            />

          </div>

        </section>


        {/* ================================================= */}
        {/* LIVE DECISION */}
        {/* ================================================= */}

        <section className="decision-section">

          <div className="section-heading">
            <div>
              <span className="eyebrow">LIVE DECISION</span>
              <h2>Workflow Execution</h2>
              <p>
                Select a ticket to inspect its complete AI decision.
              </p>
            </div>
          </div>


          <div className="decision-grid">

            {/* LEFT SIDE */}

            <div className="ticket-card">

              <div className="card-header">
                <div>
                  <span className="eyebrow">INPUT</span>
                  <h3>Customer Ticket</h3>
                </div>

                {selectedTicket && (
                  <span className="ticket-id">
                    #{selectedTicket.id}
                  </span>
                )}
              </div>


              {selectedTicket ? (

                <>
                  <div className="customer-message">
                    {selectedTicket.customer_message ||
                      "Customer message available through processing endpoint."}
                  </div>

                  <div className="metadata">

                    <InfoItem
                      label="Category"
                      value={selectedTicket.category}
                    />

                    <InfoItem
                      label="Customer Tier"
                      value={selectedTicket.customer_tier}
                    />

                    <InfoItem
                      label="Urgency"
                      value={selectedTicket.urgency}
                    />

                    <InfoItem
                      label="Expected Escalation"
                      value={selectedTicket.expected_escalation}
                    />

                  </div>

                  {!selectedPrediction && (
                    <button
                      className="process-button"
                      onClick={() =>
                        processTicket(selectedTicket.id)
                      }
                      disabled={processing}
                    >
                      {processing
                        ? "Processing..."
                        : "Run AI Workflow →"}
                    </button>
                  )}

                </>

              ) : (

                <div className="empty-state">
                  Select a ticket from the list below.
                </div>

              )}

            </div>


            {/* RIGHT SIDE */}

            <div className="decision-card">

              <div className="card-header">

                <div>
                  <span className="eyebrow">OUTPUT</span>
                  <h3>AI Decision</h3>
                </div>

                {selectedPrediction && (
                  <span
                    className={
                      selectedPrediction.reward === 1
                        ? "reward-badge success"
                        : "reward-badge failure"
                    }
                  >
                    {selectedPrediction.reward === 1
                      ? "✓ CORRECT"
                      : "✕ INCORRECT"}
                  </span>
                )}

              </div>


              {selectedPrediction ? (

                <>

                  <DecisionRow
                    label="Predicted Category"
                    value={selectedPrediction.predicted_category}
                  />

                  <DecisionRow
                    label="Predicted Urgency"
                    value={selectedPrediction.predicted_urgency}
                  />

                  <DecisionRow
                    label="Escalation Route"
                    value={selectedPrediction.predicted_escalation}
                  />

                  <DecisionRow
                    label="Reward"
                    value={
                      selectedPrediction.reward === 1
                        ? "+1"
                        : "-1"
                    }
                  />

                </>

              ) : (

                <div className="empty-state">
                  No prediction yet.
                  <br />
                  Run the AI workflow to generate one.
                </div>

              )}

            </div>

          </div>

        </section>


        {/* ================================================= */}
        {/* TICKETS */}
        {/* ================================================= */}

        <section className="tickets-section">

          <div className="section-heading">

            <div>
              <span className="eyebrow">DATASET</span>
              <h2>Enterprise Ticket Environment</h2>
              <p>
                Select any ticket to inspect its workflow.
              </p>
            </div>

            <span className="count-badge">
              {tickets.length} TICKETS
            </span>

          </div>


          <div className="ticket-list">

            {tickets.slice(0, 20).map((ticket) => {

              const prediction = predictions.find(
                (p) => p.ticket_id === ticket.id
              );

              const selected =
                selectedTicket?.id === ticket.id;

              return (

                <button
                  key={ticket.id}
                  className={`ticket-row ${
                    selected ? "selected" : ""
                  }`}
                  onClick={() => selectTicket(ticket)}
                >

                  <span className="row-id">
                    #{ticket.id}
                  </span>

                  <span className="row-category">
                    {ticket.category}
                  </span>

                  <span className="row-tier">
                    {ticket.customer_tier}
                  </span>

                  <span
                    className={`urgency ${ticket.urgency}`}
                  >
                    {ticket.urgency}
                  </span>

                  <span className="row-escalation">
                    {ticket.expected_escalation}
                  </span>

                  <span className="row-result">

                    {prediction ? (

                      prediction.reward === 1 ? (
                        <span className="result correct">
                          ✓
                        </span>
                      ) : (
                        <span className="result incorrect">
                          ✕
                        </span>
                      )

                    ) : (

                      <span className="result pending">
                        —
                      </span>

                    )}

                  </span>

                </button>

              );

            })}

          </div>

        </section>


        {/* ================================================= */}
        {/* FOOTER */}
        {/* ================================================= */}

        <footer>

          <span>
            Enterprise Workflow RL Environment
          </span>

          <span>
            FastAPI · PostgreSQL · Gemini · React
          </span>

        </footer>

      </main>

    </div>
  );
}


/* ========================================================= */
/* COMPONENTS */
/* ========================================================= */

function MetricCard({ label, value, description }) {

  return (

    <div className="metric-card">

      <span className="metric-label">
        {label}
      </span>

      <strong className="metric-value">
        {value}
      </strong>

      <span className="metric-description">
        {description}
      </span>

    </div>

  );
}


function WorkflowNode({
  number,
  title,
  subtitle,
  icon,
  active,
}) {

  return (

    <div className={`workflow-node ${active ? "active" : ""}`}>

      <div className="node-number">
        {number}
      </div>

      <div className="node-icon">
        {icon}
      </div>

      <strong>{title}</strong>

      <span>{subtitle}</span>

    </div>

  );

}


function WorkflowArrow() {

  return (

    <div className="workflow-arrow">
      →
    </div>

  );

}


function InfoItem({ label, value }) {

  return (

    <div className="info-item">

      <span>{label}</span>

      <strong>{value}</strong>

    </div>

  );

}


function DecisionRow({ label, value }) {

  return (

    <div className="decision-row">

      <span>{label}</span>

      <strong>{value}</strong>

    </div>

  );

}


export default App;