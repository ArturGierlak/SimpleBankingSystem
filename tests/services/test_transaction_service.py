import pytest
from decimal import Decimal
from app.services.transactions import TransactionService
from app.models.enums.transaction_type import TransactionType
from app.exceptions import NegativeAmountError, InsufficientFundsError, UnknownOperation


class DummyClient:
    def __init__(self, balance):
        self.initial_balance = balance


def test_create_transaction_deposit(mocker):
    db = mocker.Mock()

    mock_client_repo = mocker.patch("app.services.transactions.ClientRepository").return_value

    mock_transaction_repo = mocker.patch("app.services.transactions.TransactionRepository").return_value

    mock_client_repo.get.return_value = DummyClient(balance=Decimal("100"))

    mock_transaction_repo.create.return_value = {
        "id": 1,
        "client_id": 123,
        "amount": Decimal("50"),
        "transaction_type": TransactionType.DEPOSIT,
        "balance_after": Decimal("150"),
    }

    service = TransactionService(db)

    result = service.create_transaction(
        client_id=123,
        transaction_type=TransactionType.DEPOSIT,
        amount=Decimal("50"),
    )

    assert result["balance_after"] == Decimal("150")
    mock_client_repo.get.assert_called_once_with(123)
    mock_transaction_repo.create.assert_called_once_with(
        123, TransactionType.DEPOSIT, Decimal("50"), Decimal("150")
    )