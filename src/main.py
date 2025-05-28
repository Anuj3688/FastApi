from fastapi import FastAPI
from typing import List
from models import Tea

app = FastAPI()
teas: List[Tea] = []

@app.get("/")
def get_root():
    return { "message": "Let's Start learning! Jai Shree Ram" }

@app.get("/teas")
def get_all_teas():
    return {"success":True,"data":teas}

@app.post("/teas/add")
def add_new_tea(tea:Tea):
    teas.append(tea)
    return {"success":True,"data":f"{tea} is added"}

@app.put("/teas/{tea_id}/update",description="This will update the teas list")
def update_tea(tea_id:int,tea:Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = tea
            return {"success":True,"data":f"{tea} is modified"}
    return {"success":False,"error":"Tea not found"}


@app.delete("/teas/delete/{tea_id}",description="This will perform a delete operation on teas list")
def delete_tea(tea_id:int):
    for index,tea in enumerate(teas):
        if tea.id == tea_id:
            data = teas.pop(index)
            return {"success":True,"data":f"{data} is deleted"}
    return {"success":False,"error":"Tea not found"}

