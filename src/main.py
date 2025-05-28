from fastapi import FastAPI
from crud.crud import Crud
from models.Tea import Tea

crud_operation = Crud()

app = FastAPI()

@app.get("/")
def get_root():
    return { "message": "Let's Start learning! Jai Shree Ram" }

@app.get("/teas")
def get_all_teas():
    response = crud_operation.get_all_tea()
    return response

@app.post("/teas/add")
def add_new_tea(tea:Tea):
    message = crud_operation.add_new_tea(tea)
    return {"success":True,"data":message}

@app.put("/teas/{tea_id}/update",description="This will update the teas list")
def update_tea(tea_id:int,tea:Tea):
    response = crud_operation.update_tea(tea)
    return response

@app.delete("/teas/delete/{tea_id}",description="This will perform a delete operation on teas list")
def delete_tea(tea_id:int):
    response = crud_operation.remove_tea(tea_id)
    return response

