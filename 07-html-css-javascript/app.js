const API = "http://localhost:8000";
const list = document.querySelector("#list");

function esc(s) {                       // prevents XSS
  const d = document.createElement("div");
  d.textContent = s;
  return d.innerHTML;
}

async function loadTickets() {
  const res = await fetch(`${API}/tickets`);
  if (!res.ok) { list.innerHTML = "<li>Failed to load</li>"; return; }
  const tickets = await res.json();
  list.innerHTML = tickets.map(t => `<li>#${t.id} [${esc(t.priority)}] ${esc(t.title)}</li>`).join("");
}

document.querySelector("#form").addEventListener("submit", async e => {
  e.preventDefault();
  await fetch(`${API}/tickets`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      title: document.querySelector("#title").value,
      priority: document.querySelector("#priority").value,
    }),
  });
  e.target.reset();
  loadTickets();
});

loadTickets();
