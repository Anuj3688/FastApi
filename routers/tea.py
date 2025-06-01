from fastapi import APIRouter
from models.Tea import Tea
from crud.crud import Crud

crud_operation = Crud()
router = APIRouter(prefix="/tea", tags=["Tea"])


@router.get("/teas")
def get_all_teas():
    response = crud_operation.get_all_tea()
    return response



@router.post("/teas/add")
def add_new_tea(tea:Tea):
    message = crud_operation.add_new_tea(tea)
    return {"success":True,"data":message}

@router.put("/teas/{tea_id}/update",description="This will update the teas list")
def update_tea(tea_id:int,tea:Tea):
    response = crud_operation.update_tea(tea)
    return response

@router.delete("/teas/delete/{tea_id}",description="This will perform a delete operation on teas list")
def delete_tea(tea_id:int):
    response = crud_operation.remove_tea(tea_id)
    return response
