# app/schemas.py
from pydantic import BaseModel

class ComponentCreate(BaseModel):
    name: str
    config: str

class WorkflowCreate(BaseModel):
    name: str
    structure: str
