from decimal import Decimal

from app.schemas.client import ClientResponse
from app.services.clients import ClientService


def test_create_client(client_with_mocked_db, mocker):

    client = client_with_mocked_db

    mocked_create = mocker.patch.object(
        ClientService,
        "create_client",
        return_value=ClientResponse(
            id=1,
            first_name="Test",
            last_name="Test",
            initial_balance=Decimal("1000.0"),
        ),
    )

    payload = {"first_name": "Test", "last_name": "Test", "initial_balance": 1000.0}

    response = client.post("/clients/", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["first_name"] == "Test"
    assert data["last_name"] == "Test"
    assert float(data["initial_balance"]) == 1000.0

    mocked_create.assert_called_once_with(
        first_name="Test", last_name="Test", initial_balance=1000.0
    )
