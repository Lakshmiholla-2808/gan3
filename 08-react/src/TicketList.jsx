import { useEffect, useState } from "react";

const API = import.meta.env.VITE_API ?? "http://localhost:8000";

export default function TicketList() {
  const [tickets, setTickets] = useState([]);
  const [status, setStatus] = useState("open");
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`${API}/tickets?status=${status}`)
      .then(r => (r.ok ? r.json() : Promise.reject(new Error("Request failed"))))
      .then(setTickets)
      .catch(setError);
  }, [status]);

  if (error) return <p>Error: {error.message}</p>;

  return (
    <section>
      <select value={status} onChange={e => setStatus(e.target.value)}>
        <option value="open">Open</option>
        <option value="closed">Closed</option>
      </select>
      <ul>
        {tickets.map(t => (
          <li key={t.id}>#{t.id} [{t.priority}] {t.title}</li>
        ))}
      </ul>
    </section>
  );
}
