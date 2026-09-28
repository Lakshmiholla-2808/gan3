-- 1. Open P1 tickets
SELECT * FROM tickets WHERE status='open' AND priority='P1';

-- 2. Tickets per agent
SELECT a.name, COUNT(*) AS open_tickets
FROM tickets t JOIN agents a ON a.id = t.agent_id
WHERE t.status='open'
GROUP BY a.name HAVING COUNT(*) >= 1
ORDER BY open_tickets DESC;

-- 3. Average resolution time by priority
SELECT priority, AVG(hours_to_resolve) FROM tickets
WHERE hours_to_resolve IS NOT NULL GROUP BY priority;

-- 4. Agents with no tickets (LEFT JOIN)
SELECT a.name FROM agents a LEFT JOIN tickets t ON t.agent_id=a.id
WHERE t.id IS NULL;

-- 5. Unassigned tickets
SELECT title FROM tickets WHERE agent_id IS NULL;

-- Your turn: write questions 6-15 (see labs in README).
