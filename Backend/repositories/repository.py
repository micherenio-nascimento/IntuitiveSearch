import csv
from typing import List
from app.models.operator import Operator

class OperatorRepository:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.operators = self._load_operators()

    def _load_operators(self) -> List[Operator]:
        operators = []
        with open(self.file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                operators.append(Operator(**row))
        return operators

    def search(self, query: str) -> List[Operator]:
        query = query.lower()
        return [
            op for op in self.operators
            if (query in op.Razao_Social.lower() or
                query in op.Nome_Fantasia.lower() or
                query in op.CNPJ or
                query in op.Registro_ANS)
        ]
