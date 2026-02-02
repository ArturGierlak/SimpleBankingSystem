from decimal import Decimal

from sqlalchemy.orm import Session

from app.repositories.clients import ClientRepository


class ClientService:

    def __init__(self, db: Session):
        self.repo = ClientRepository(db)

    def create_client(self, first_name: str, last_name: str, initial_balance: Decimal):
        return self.repo.create(first_name, last_name, initial_balance)

    def get_client(self, client_id: int):
        return self.repo.get(client_id)

    def list_clients(self):
        return self.repo.list()

    def delete_client(self, client_id):
        return self.repo.delete(client_id)
