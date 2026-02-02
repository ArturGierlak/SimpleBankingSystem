from datetime import datetime
from decimal import Decimal

from app.models.enums.transaction_type import TransactionType
from app.schemas.transaction import TransactionResponse
from app.services.transactions import TransactionService


def test_create_transaction(client_with_mocked_db, mocker):

    client = client_with_mocked_db

    mocked_create = mocker.patch.object(
        TransactionService,
        "create_transaction",
        return_value=TransactionResponse(
            id=1,
            client_id=123,
            transaction_type="deposit",
            amount=100.0,
            timestamp=datetime(2024, 1, 1, 12, 0),
            balance_after=Decimal("1000.0"),
        ),
    )

    payload = {"client_id": 123, "transaction_type": "deposit", "amount": 100.0}

    response = client.post("/transactions/", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["client_id"] == 123
    assert data["transaction_type"] == "deposit"
    assert float(data["amount"]) == 100.0
    assert "timestamp" in data
    assert "balance_after" in data

    mocked_create.assert_called_once_with(
        client_id=123, transaction_type="deposit", amount=100.0
    )


def test_list_client_transactions(client_with_mocked_db, mocker):
    client = client_with_mocked_db

    mocked_list = mocker.patch.object(
        TransactionService,
        "list_client_transactions",
        return_value=[
            TransactionResponse(
                id=1,
                client_id=123,
                transaction_type="deposit",
                amount=50.0,
                timestamp=datetime(2024, 1, 1, 12, 0),
                balance_after=Decimal("150.0"),
            )
        ],
    )

    response = client.get("/transactions/123")

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert data[0]["client_id"] == 123
    assert float(data[0]["amount"]) == 50.0

    mocked_list.assert_called_once_with(123)


def test_list_all_transactions(client_with_mocked_db, mocker):
    client = client_with_mocked_db

    mocked_list_all = mocker.patch.object(
        TransactionService,
        "list_all_transactions",
        return_value=[
            TransactionResponse(
                id=10,
                client_id=999,
                transaction_type=TransactionType.DEPOSIT,
                amount=20.0,
                timestamp=datetime(2024, 1, 1, 10, 0),
                balance_after=Decimal("80.0"),
            )
        ],
    )

    response = client.get("/transactions/")

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert data[0]["id"] == 10
    assert data[0]["client_id"] == 999

    mocked_list_all.assert_called_once()
