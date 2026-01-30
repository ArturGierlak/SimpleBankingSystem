from decimal import Decimal
from app.repositories.transactions import TransactionRepository
from app.models.client import Client
from app.models.enums.transaction_type import TransactionType


def test_create_transaction_success(db_session):
    repo = TransactionRepository(db_session)

    client = Client(id=1, first_name="Test", last_name="Test", initial_balance=Decimal("100"))
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