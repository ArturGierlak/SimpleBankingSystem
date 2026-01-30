import pytest
from fastapi.testclient import TestClient
from app.services.transactions import TransactionService
from app.schemas.transaction import TransactionResponse
from datetime import datetime
from decimal import Decimal
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
        )
    )

    payload = {
        "client_id": 123,
        "transaction_type": "deposit",
        "amount": 100.0
    }

    
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
        client_id=123,
        transaction_type="deposit",
        amount=100.0
    )