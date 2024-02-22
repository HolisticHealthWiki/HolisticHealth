from starlette.testclient import TestClient

from HolisticHealth.__main__ import app

client = TestClient(app)


def test_read_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Production": "True"}
