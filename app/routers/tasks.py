from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.core.deps import get_current_user

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.get("/")
def get_tasks(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return {
        "user": user,
        "tasks": []
    }