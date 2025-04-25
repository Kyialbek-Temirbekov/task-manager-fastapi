from fastapi import Depends, APIRouter, Response
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from ...db.database import get_db
from ...db.db_structure import Task
from ..schemas.task import TaskCreate, TaskResponse

router = APIRouter()

@router.post("")
def create_task(task_sc: TaskCreate, db: Session = Depends(get_db)):
    task = Task(**task_sc.dict())
    db.add(task)
    db.commit()
    db.refresh(task)
    return Response(status_code=200)