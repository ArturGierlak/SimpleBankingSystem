import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.db import get_db
from app.main import app
from app.models.base import Base


@pytest.fixture
def mocked_db(mocker):
    return mocker.Mock()


@pytest.fixture
def client_with_mocked_db(mocked_db):
    def override_get_db():
        yield mocked_db

    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


@pytest.fixture
def db_session():
    engine = create_engine("sqlite:///:memory:", echo=False)
    Base.metadata.create_all(engine)

    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

    yield session

    session.close()
