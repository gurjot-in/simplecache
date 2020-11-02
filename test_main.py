from fastapi.testclient import TestClient
import pytest
from main import app
from httpx import AsyncClient
import time
client = TestClient(app)


def test_get_all_keys():
    client.post("/cache", json={"key": "tomato", "value": "$12"})
    response = client.get("/cache")
    assert response.status_code == 200
    assert response.json() == ["tomato"]
    client.delete("/cache/tomato")


def test_delete_key():
    client.post("/cache", json={"key": "apple", "value": "$13"})
    response = client.get("/cache/apple")
    assert response.status_code == 200
    assert response.json() == "$13"

    client.delete("/cache/apple")
    response = client.get("/cache/apple")

    assert response.status_code == 200
    assert response.json() is None


def test_insert_with_expiry():
    client.post("/cache", json={"key": "apple", "value": "$13", "ttl": 3})
    response = client.get("/cache/apple")
    assert response.status_code == 200
    assert response.json() == '$13'

    time.sleep(3)
    response = client.get("/cache/apple")
    print(response.json())
    assert response.status_code == 200
    assert response.json() is None

