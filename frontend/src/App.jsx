import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

const API = "http://127.0.0.1:8000";

function App() {
  const [metrics, setMetrics] = useState(null);
  const [tickets, setTickets] = useState([]);
  const [predictions, setPredictions] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
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
      } catch (error) {
        console.error("Dashboard loading failed:", error);
      } finally {
        setLoading(false);
      }
    }

    loadDashboard();
  }, []);

  if (loading) {
    return <div className="loading">Loading Enterprise Workflow...</div>;
  }

  return (
    <div className="app">
      <header className="header">
        <div>
          <h1>Enterprise Workflow AI</h1>
          <p>AI-powered customer support routing & evaluation</p>
        </div>

        <div className="status">
          <span className="status-dot"></span>
          API Online
        </div>
      </header>

      <main className="container">
        <section className="stats">
          <div className="card">
            <span>Total Tickets</span>
            <strong>{tickets.length}</strong>
          </div>

          <div className="card">
            <span>Predictions</span>
            <strong>{metrics?.total_predictions ?? 0}</strong>
          </div>

          <div className="card">
            <span>Accuracy</span>
            <strong>
              {((metrics?.accuracy ?? 0) * 100).toFixed(0)}%
            </strong>
          </div>

          <div className="card">
            <span>Average Reward</span>
            <strong>
              {(metrics?.average_reward ?? 0).toFixed(2)}
            </strong>
          </div>
        </section>

        <section className="panel">
          <div className="panel-header">
            <div>
              <h2>AI Predictions</h2>
              <p>Latest workflow routing decisions</p>
            </div>

            <span className="badge">
              {predictions.length} records
            </span>
          </div>

          <div className="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Ticket</th>
                  <th>Category</th>
                  <th>Urgency</th>
                  <th>Escalation</th>
                  <th>Reward</th>
                </tr>
              </thead>

              <tbody>
                {predictions.map((prediction) => (
                  <tr key={prediction.id}>
                    <td>#{prediction.id}</td>
                    <td>Ticket #{prediction.ticket_id}</td>
                    <td>{prediction.predicted_category}</td>
                    <td>
                      <span
                        className={`urgency ${prediction.predicted_urgency}`}
                      >
                        {prediction.predicted_urgency}
                      </span>
                    </td>
                    <td>{prediction.predicted_escalation}</td>
                    <td>
                      <span className="reward">
                        {prediction.reward === 1 ? "✓ 1" : "✗ 0"}
                      </span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>

        <section className="panel">
          <div className="panel-header">
            <div>
              <h2>Ticket Dataset</h2>
              <p>100 synthetic enterprise support tickets</p>
            </div>
          </div>

          <div className="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Category</th>
                  <th>Customer Tier</th>
                  <th>Urgency</th>
                  <th>Expected Escalation</th>
                </tr>
              </thead>

              <tbody>
                {tickets.slice(0, 20).map((ticket) => (
                  <tr key={ticket.id}>
                    <td>#{ticket.id}</td>
                    <td>{ticket.category}</td>
                    <td>{ticket.customer_tier}</td>
                    <td>
                      <span
                        className={`urgency ${ticket.urgency}`}
                      >
                        {ticket.urgency}
                      </span>
                    </td>
                    <td>{ticket.expected_escalation}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;