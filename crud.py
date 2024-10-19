# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas

def create_component(db: Session, component: schemas.ComponentCreate):
    db_component = models.Component(**component.dict())
    db.add(db_component)
    db.commit()
    db.refresh(db_component)
    return db_component

def create_workflow(db: Session, workflow: schemas.WorkflowCreate):
    db_workflow = models.Workflow(**workflow.dict())
    db.add(db_workflow)
    db.commit()
    db.refresh(db_workflow)
    return db_workflow
