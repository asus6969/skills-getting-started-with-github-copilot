from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_removes_participant():
    response = client.delete("/activities/Chess Club/unregister?email=michael@mergington.edu")

    assert response.status_code == 200
    data = response.json()
    assert "Unregistered michael@mergington.edu from Chess Club" in data["message"]

    activities = client.get("/activities").json()
    assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]


def test_unregister_missing_participant_returns_400():
    response = client.delete("/activities/Gym Class/unregister?email=missing@mergington.edu")

    assert response.status_code == 400
