from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_get_activities_returns_expected_backend_data():
    response = client.get("/activities")

    assert response.status_code == 200

    data = response.json()
    assert "Chess Club" in data
    assert "Programming Class" in data
    assert "Gym Class" in data

    chess_club = data["Chess Club"]
    assert chess_club["description"]
    assert chess_club["schedule"]
    assert isinstance(chess_club["participants"], list)
