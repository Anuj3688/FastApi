from fastapi import APIRouter, UploadFile, File, HTTPException
from crud.crud import Crud

crud_operation = Crud()

router = APIRouter()


@router.post("/upload", description="Just Checking")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Invalid file type. Only CSV is allowed.")

    contents = await file.read()
    crud_operation.add_tea_in_bulk(contents)
    return {"filename": file.filename, "size": len(contents)}
