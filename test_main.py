from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_zipcode_validate_with_good_zipcode():
    response = client.get("/zipcode/EC1A%201BB/validate")
    assert response.status_code == 200
    assert response.json() == {"zipcode": "EC1A 1BB", "is_valid": "True"}


def test_zipcode_validate_with_bad_zipcode():
    response = client.get("/zipcode/EC1A1B1/validate")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid zipcode EC1A1B1"}


def test_zipcode_format_with_good_zipcode():
    response = client.get("/zipcode/EC1A1BB/format")
    assert response.status_code == 200
    assert response.json() == {"formatted_zipcode": "EC1A 1BB", "zipcode": "EC1A1BB"}


def test_zipcode_format_with_bad_zipcode():
    response = client.get("/zipcode/123/format")
    assert response.status_code == 400
    assert response.json() == {"detail": "Unable to format 123"}