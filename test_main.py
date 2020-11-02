from fastapi.testclient import TestClient

from fapi import app
from httpx import AsyncClient

client = TestClient(app)


def test_get_all_keys():
    client.post("/cache", json={"key": "tomato", "value": "$12"})
    response = client.get("/cache")
    assert response.status_code == 200
    assert response.json() == ["tomato"]


def test_delete_key():
    client.post("/cache", json={"key": "apple", "value": "$13"})
    response = client.get("/cache/apple")
    assert response.status_code == 200
    assert response.json() == "apple"

    client.delete("/cache/apple")
    response = client.get("/cache/apple")

    assert response.status_code == 200
    assert response.json() is None


def test_large_input():
    for i in range(10000000):
        client.post("/cache", json={"key": "k_{}".format(i), "value": "v_{}".format(i)})

    response = client.get("/cache")
    assert response.status_code == 200
    assert len(response.json()) == 10000000

