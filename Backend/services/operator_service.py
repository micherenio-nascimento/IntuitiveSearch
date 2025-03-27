from repositories.operator_repository import OperatorRepository
from typing import List, Optional
from models.operator import Operator

class OperatorService:
    def __init__(self, repository: OperatorRepository):
        self.repository = repository

    def search_operators(self, query: Optional[str] = None, razao_social: Optional[str] = None,
                          nome_fantasia: Optional[str] = None, cnpj: Optional[str] = None,
                          registro_ans: Optional[str] = None) -> List[Operator]:
    
        filtered_operators = self.repository.operators
        
        if query:
            filtered_operators = [
                op for op in filtered_operators
                if (query.lower() in op.Razao_Social.lower() or
                    query.lower() in op.Nome_Fantasia.lower() or
                    query in op.CNPJ or
                    query in op.Registro_ANS)
            ]
        
        if razao_social:
            filtered_operators = [
                op for op in filtered_operators if razao_social.lower() in op.Razao_Social.lower()
            ]

        if nome_fantasia:
            filtered_operators = [
                op for op in filtered_operators if nome_fantasia.lower() in op.Nome_Fantasia.lower()
            ]

        if cnpj:
            filtered_operators = [
                op for op in filtered_operators if cnpj in op.CNPJ
            ]

        if registro_ans:
            filtered_operators = [
                op for op in filtered_operators if registro_ans in op.Registro_ANS
            ]

        return filtered_operators
