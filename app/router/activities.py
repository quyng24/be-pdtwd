from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..schema.activities import ActivitiesCreate, ActivitiesResponse
from app.curd.activities import create_activity, get_all_activities

router = APIRouter(prefix="/activities", tags=["Activities"])


@router.post("/", response_model=ActivitiesResponse)
def create(data: ActivitiesCreate, db: Session = Depends(get_db)):
    return create_activity(db, data)


@router.get("/", response_model=list[ActivitiesResponse])
def list_all(db: Session = Depends(get_db)):
    return get_all_activities(db)
