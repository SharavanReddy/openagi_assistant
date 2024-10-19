from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# in-memory data storage
llms = []
agents = []
tools = []
workflows = []
stacks = []



# Pydantic models

class Stack(BaseModel):
    id: int
    name: str
    description: str

class LLM(BaseModel):
    id: int
    name: str
    description: str

class Agent(BaseModel):
    id: int
    name: str
    description: str

class Tool(BaseModel):
    id: int
    name: str
    description: str

class Workflow(BaseModel):
    id: int
    name: str
    description: str
    components: List[int]  # List of component IDs


@app.get("/")
async def read_root():
    return {"message": "Welcome to OpenAGI!"}

@app.get("/home")
async def read_home_page():
    return {"message": "Welcome to the Home Page"}

@app.get("/build-stack")
async def read_build_stack_page():
    return {"message": "Build your Stack here"}

@app.get("/run-stack")
async def read_run_stack_page():
    return {"message": "Run your Stack here"}

@app.get("/stacks", response_model=List[Stack])
async def read_stacks_page():
    return stacks

@app.get("/stack-details/{stack_id}", response_model=Stack)
async def read_stack_details_page(stack_id: int):
    for stack in stacks:
        if stack['id'] == stack_id:
            return stack
    raise HTTPException(status_code=404, detail="Stack not found")

# Endpoints for managing LLMs
@app.get("/llms", response_model=List[LLM])
async def get_llms():
    return llms
