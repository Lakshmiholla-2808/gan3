# React (8 days)

| Day | Topics |
|---|---|
| 1 | Vite setup, JSX, components, props |
| 2 | useState, events, lists and keys |
| 3 | useEffect, data fetching, loading/error states |
| 4 | Controlled forms, validation |
| 5 | React Router, protected routes |
| 6 | Context API, custom hooks, auth state |
| 7 | TanStack Query, styling (Tailwind or a component library) |
| 8 | Testing basics, build and deploy |

## Setup
```bash
npm create vite@latest support-ui -- --template react
cd support-ui && npm install && npm run dev
```
Copy `src/TicketList.jsx` and `src/App.jsx` from this folder into the new project.
Set the API base URL in `.env` as `VITE_API=http://localhost:8000`.
