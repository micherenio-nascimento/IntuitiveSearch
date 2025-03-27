from fastapi import APIRouter, Depends
from services.operator_service import OperatorService
from repositories.operator_repository import OperatorRepository
from typing import Optional

router = APIRouter()

repository = OperatorRepository("data/Relatorio_cadop_ficticio.csv")
service = OperatorService(repository)

@router.get("/operators/search")
async def search_operators(query: Optional[str] = None, 
                            razao_social: Optional[str] = None, 
                            nome_fantasia: Optional[str] = None, 
                            cnpj: Optional[str] = None, 
                            registro_ans: Optional[str] = None):
    """Endpoint para buscar operadores com filtros"""
    results = service.search_operators(query, razao_social, nome_fantasia, cnpj, registro_ans)
    return {"operators": [op.dict() for op in results]}
