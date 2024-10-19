# app/routers/components.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/components/", response_model=schemas.ComponentCreate)
def create_component(component: schemas.ComponentCreate, db: Session = Depends(get_db)):
    return crud.create_component(db=db, component=component)
