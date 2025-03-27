from fastapi import APIRouter, Depends
from services.operator_service import OperatorService
from repositories.operator_repository import OperatorRepository

router = APIRouter()

repository = OperatorRepository("data/Relatorio_cadop_ficticio.csv")
service = OperatorService(repository)

@router.get("/operators/search")
async def search_operators(query: str):
    """Endpoint para buscar operadores"""
    results = service.search_operators(query)
    return {"operators": [op.dict() for op in results]}
