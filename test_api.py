import requests
import pytest

# Замените BASE_URL на реальный URL вашего API
BASE_URL = "http://api.example.com"

def test_get_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_user_valid():
    user_data = {"name": "John Doe", "email": "john@example.com"}
    response = requests.post(f"{BASE_URL}/users", json=user_data)
    assert response.status_code == 201

def test_create_user_invalid():
    invalid_data = {"name": "", "email": "invalid"}
    response = requests.post(f"{BASE_URL}/users", json=invalid_data)
    assert response.status_code == 400

def test_get_user_by_id():
    user_id = 1  # Предполагается, что пользователь с id=1 существует
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id

def test_get_user_not_found():
    response = requests.get(f"{BASE_URL}/users/9999")
    assert response.status_code == 404

def test_update_user():
    user_id = 1
    updated_data = {"name": "Jane Doe", "email": "jane@example.com"}
    response = requests.put(f"{BASE_URL}/users/{user_id}", json=updated_data)
    assert response.status_code == 200

def test_update_user_not_found():
    response = requests.put(f"{BASE_URL}/users/9999", json={"name": "Test", "email": "test@example.com"})
    assert response.status_code == 404

def test_delete_user():
    user_id = 1
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 204

def test_delete_user_not_found():
    response = requests.delete(f"{BASE_URL}/users/9999")
    assert response.status_code == 404




Эти тесты проверяют корректность работы API в соответствии со спецификацией.
