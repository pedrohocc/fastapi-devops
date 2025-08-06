def test_create_user(client):
    response = client.post("/users", json={
        "name": "John Doe",
        "email": "john@example.com"
    })
    assert response.status_code == 201
