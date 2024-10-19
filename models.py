# app/models.py
from sqlalchemy import Column, Integer, String
from .database import Base

class Component(Base):
    __tablename__ = "components"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    config = Column(String)

class Workflow(Base):
    __tablename__ = "workflows"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    structure = Column(String)
