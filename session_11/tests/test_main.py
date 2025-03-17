# Create a test file named test_main.py:

from fastapi.testclient import TestClient
from src.session_11.main import app, Item

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"item": {"name": "Test Item"}}


def test_create_item_success():
    response = client.post("/items/", json={"name": "Test Item"})
    assert response.status_code == 200
    assert response.json() == {"item": {"name": "Test Item"}}

def test_update_id(item_id: int, item: Item):
    response = client.put("/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"Item_name": item.name, "item_id": item_id}


def test_create_item_failure():
    response = client.post("/items/", json={"description": "No name provided"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Item must have a name"
