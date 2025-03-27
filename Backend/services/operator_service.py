from repositories.operator_repository import OperatorRepository
from typing import List
from models.operator import Operator

class OperatorService:
    def __init__(self, repository: OperatorRepository):
        self.repository = repository

    def search_operators(self, query: str):
        return self.repository.search(query)