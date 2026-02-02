from decimal import Decimal

import pytest

from app.exceptions import ClientNotFound, InsufficientFundsError
from app.models.client import Client
from app.models.enums.transaction_type import TransactionType
from app.models.transaction import Transaction
from app.repositories.transactions import TransactionRepository


def test_create_transaction_success(db_session):
    repo = TransactionRepository(db_session)

    client = Client(
        id=1, first_name="Test", last_name="Test", initial_balance=Decimal("100")
    )
    db_session.add(client)
    db_session.commit()

    t = repo.create(
        client_id=1,
        transaction_type=TransactionType.DEPOSIT,
        amount=Decimal("50"),
        balance_after=Decimal("150"),
    )

    assert t.id is not None
    assert t.client_id == 1
    assert t.amount == Decimal("50")
    assert t.balance_after == Decimal("150")
    assert t.transaction_type == TransactionType.DEPOSIT


def test_create_transaction_client_not_found(db_session):
    repo = TransactionRepository(db_session)

    with pytest.raises(ClientNotFound):
        repo.create(
            client_id=999,
            transaction_type=TransactionType.DEPOSIT,
            amount=Decimal("50"),
            balance_after=Decimal("150"),
        )


def test_create_transaction_negative_balance(db_session):
    repo = TransactionRepository(db_session)

    client = Client(
        id=1, first_name="Test", last_name="Test", initial_balance=Decimal("100")
    )
    db_session.add(client)
    db_session.commit()

    with pytest.raises(InsufficientFundsError):
        repo.create(
            client_id=1,
            transaction_type=TransactionType.WITHDRAWAL,
            amount=Decimal("200"),
            balance_after=Decimal("-100"),
        )


def test_list_transactions_for_client(db_session):
    repo = TransactionRepository(db_session)

    client = Client(id=1, first_name="Test", last_name="Test", initial_balance=100)
    db_session.add(client)
    db_session.commit()

    t1 = Transaction(
        client_id=1,
        transaction_type=TransactionType.DEPOSIT,
        amount=10,
        balance_after=110,
    )
    t2 = Transaction(
        client_id=1,
        transaction_type=TransactionType.WITHDRAWAL,
        amount=5,
        balance_after=105,
    )
    db_session.add_all([t1, t2])
    db_session.commit()

    result = repo.list(1)

    assert len(result) == 2
    assert all(t.client_id == 1 for t in result)


def test_list_transactions_client_not_found(db_session):
    repo = TransactionRepository(db_session)

    with pytest.raises(ClientNotFound):
        repo.list(client_id=123)


def test_list_all_transactions(db_session):
    repo = TransactionRepository(db_session)

    client = Client(id=1, first_name="Test", last_name="Test", initial_balance=100)
    db_session.add(client)
    db_session.commit()

    db_session.add(
        Transaction(
            client_id=1,
            transaction_type=TransactionType.DEPOSIT,
            amount=10,
            balance_after=110,
        )
    )
    db_session.add(
        Transaction(
            client_id=1,
            transaction_type=TransactionType.WITHDRAWAL,
            amount=5,
            balance_after=105,
        )
    )
    db_session.commit()

    result = repo.list_all()

    assert len(result) == 2
