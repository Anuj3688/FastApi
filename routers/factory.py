from fastapi import APIRouter
from models.FactoryStocks import FactoryStocks
from crud.crud import Crud

crud_operation = Crud()

router = APIRouter(prefix="/factory", tags=["Factory"])


@router.get("/factory")
def get_all_factory():
    response = crud_operation.get_all_factory()
    return response


@router.post("/Factory/add", description="Need to add factory name and product details")
def add_new_factory(factory: FactoryStocks):
    response = crud_operation.add_factory_details(factory)
    return response
