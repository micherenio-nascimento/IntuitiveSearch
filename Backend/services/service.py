from app.repositories.operator_repository import OperatorRepository

class OperatorService:
    def __init__(self, repository: OperatorRepository):
        self.repository = repository

    def search_operators(self, query: str):
        return self.repository.search(query)