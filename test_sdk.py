import pytest
from verify_eligibility import EligibilityClient

@pytest.fixture
def client():
    return EligibilityClient(base_url="http://localhost:8000")

def test_verify_eligibility_success(client):
    response = client.verify(
        carrier_name="Test Carrier",
        member_id="111111",
        full_name="Erol Kaan",
        dob="2023-02-03"
    )
    assert "eligible" in response
    assert isinstance(response["eligible"], bool)

def test_verify_eligibility_invalid_input(client):
    response = client.verify(
        carrier_name="",
        member_id="",
        full_name="",
        dob="invalid-date"
    )
    assert "eligible" not in response
    assert "message" in response
    assert response["message"] == "Invalid input"

def test_verify_eligibility_not_eligible(client):
    response = client.verify(
        carrier_name="Non-Existent Carrier",
        member_id="000000",
        full_name="John Doe",
        dob="1980-01-01"
    )
    assert "eligible" in response
    assert response["eligible"] is False
    assert "message" in response
    assert isinstance(response["message"], str)
