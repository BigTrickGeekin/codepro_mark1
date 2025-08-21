from fastapi.testclient import TestClient
from backend.main import app, _tasks

client = TestClient(app)


def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"ok": True}


def test_task_flow():
    _tasks.clear()
    res = client.post("/tasks", json={"id": 1, "text": "hi"})
    assert res.status_code == 200
    assert res.json()["text"] == "hi"

    res = client.get("/tasks")
    assert res.status_code == 200
    assert res.json() == [{"id": 1, "text": "hi"}]

    res = client.post("/tasks", json={"id": 1, "text": "dup"})
    assert res.status_code == 400


def test_cors_preflight():
    res = client.options(
        "/tasks",
        headers={
            "Origin": "http://example.com",
            "Access-Control-Request-Method": "POST",
        },
    )
    assert res.status_code == 200
    assert res.headers["access-control-allow-origin"] == "*"
