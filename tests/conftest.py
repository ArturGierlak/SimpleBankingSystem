import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database.db import get_db

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
