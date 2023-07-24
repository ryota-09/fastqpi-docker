from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import api.cruds.task as task_crud
import api.schemas.task as task_schema
from api.db import get_db

router = APIRouter()

@router.get("/tasks", response_model=list[task_schema.Task])
async def list_tasks():
  return [task_schema.Task(id=1, title="1つ目のtodoタスク")]

@router.post("/tasks", response_model=task_schema.TaskCreate)
async def create_task(task_body: task_schema.TaskCreate, db: Session = Depends(get_db)):
  # dict ==> model_dump
  return task_crud.create_task(db, task_body)

@router.put("/tasks/{task_id}", response_model=task_schema.TaskCreate)
async def update_task(task_id: int, task_body: task_schema.TaskCreate):
  return task_schema.TaskCreateResponse(id=task_id, **task_body.dict())

@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task(task_id: int):
  return 

@router.put("/tasks/{task_id}/done", response_model=None)
async def mark_task_as_done(task_id: int):
  return

@router.delete("/tasks/{task_id}/done", response_model=None)
async def unmark_task_as_done(task_id: int):
  return 
