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
