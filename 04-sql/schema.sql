CREATE TABLE agents (id INTEGER PRIMARY KEY, name TEXT NOT NULL);
CREATE TABLE tickets (
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  priority TEXT NOT NULL DEFAULT 'P4',
  status TEXT NOT NULL DEFAULT 'open',
  agent_id INTEGER REFERENCES agents(id),
  hours_to_resolve REAL
);
INSERT INTO agents VALUES (1,'Asha'),(2,'Ravi'),(3,'Meena');
INSERT INTO tickets (title,priority,status,agent_id,hours_to_resolve) VALUES
 ('VPN down','P1','open',1,NULL),
 ('Password reset','P3','closed',2,1.5),
 ('Laptop slow','P2','open',1,NULL),
 ('Email bounce','P2','closed',3,6),
 ('Printer jam','P4','open',NULL,NULL);
