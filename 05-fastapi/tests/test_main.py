from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_and_read():
    r = client.post("/tickets", json={"title": "VPN down", "priority": "P1"})
    assert r.status_code == 201
    tid = r.json()["id"]
    assert client.get(f"/tickets/{tid}").json()["title"] == "VPN down"


def test_not_found():
    assert client.get("/tickets/9999").status_code == 404


def test_close():
    tid = client.post("/tickets", json={"title": "x"}).json()["id"]
    assert client.patch(f"/tickets/{tid}/close").json()["status"] == "closed"
