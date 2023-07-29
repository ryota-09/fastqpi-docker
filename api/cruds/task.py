from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session
import api.models.task as task_model
import api.schemas.task as task_schema

def create_task(db: Session, task_create: task_schema.TaskCreate) -> task_model.Task:
  task = task_model.Task(**task_create.model_dump())
  db.add(task)
  db.commit()
  db.refresh(task)
  return task

def get_tasks_with_done(db: Session) -> task_model.Task:
  result: Result = db.execute(
    select(
      task_model.Task.id,
      task_model.Task.title,
      task_model.Done.id.isnot(None).label("done"),
    ).outerjoin(task_model.Done)
  )
  return result.all()

def get_task(db: Session, task_id: int) -> task_model.Task | None:
  print(f"@@@@@@@@@@@{task_id}")
  result : Result = db.execute(
    select(task_model.Task).filter(task_model.Task.id == task_id)
  )
  return result.scalar()

def update_task(db: Session, task_create: task_schema.TaskCreate, original: task_model.Task) -> task_model.Task:
  original.title = task_create.title
  db.add(original)
  db.commit()
  db.refresh(original)
  return original

def delete_task(db: Session, original: task_model.Task) -> None:
  db.delete(original)
  db.commit()
