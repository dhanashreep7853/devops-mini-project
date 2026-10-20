import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"


def test_home_page(client):
    r = client.get("/")
    assert r.status_code == 200
    assert b"Task Tracker" in r.data


def test_add_and_list_task(client):
    r = client.post("/api/tasks", json={"title": "Write report"})
    assert r.status_code == 201
    assert r.get_json()["title"] == "Write report"
    tasks = client.get("/api/tasks").get_json()
    assert len(tasks) == 1 and tasks[0]["done"] is False


def test_add_task_requires_title(client):
    r = client.post("/api/tasks", json={"title": "   "})
    assert r.status_code == 400


def test_toggle_task(client):
    tid = client.post("/api/tasks", json={"title": "x"}).get_json()["id"]
    assert client.patch(f"/api/tasks/{tid}").get_json()["done"] is True
    assert client.patch(f"/api/tasks/{tid}").get_json()["done"] is False


def test_delete_task(client):
    tid = client.post("/api/tasks", json={"title": "x"}).get_json()["id"]
    assert client.delete(f"/api/tasks/{tid}").status_code == 204
    assert client.get("/api/tasks").get_json() == []


def test_missing_task_404(client):
    assert client.patch("/api/tasks/99").status_code == 404
    assert client.delete("/api/tasks/99").status_code == 404
