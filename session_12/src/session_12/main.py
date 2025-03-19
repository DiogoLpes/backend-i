from typing import Annotated
from fastapi.responses import JSONResponse
from src.session_12.models import Task
from fastapi import FastAPI


api = FastAPI(
    title = "TODO Etic_Algarve API"
)



@api.post("/task")
def create_task(data: Annotated{Task.Form()}):
    return JSONResponse({"status": "created"}, status_code=status.HTTP_201_CREATED)

@api.get("/task", response_model=Task)
def list_task():
    pass

@api.put("/task")
def edit_task():
    pass

@api.patch("/task")
def close_task():
    pass

@api.delete("/task")
def delete_task():
    pass    