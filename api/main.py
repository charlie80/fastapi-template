from typing import List, Optional

from fastapi import Depends, FastAPI
from starlette.responses import RedirectResponse
from starlette.status import HTTP_201_CREATED

from api.repository import Todo, TodoFilter, TodoRepository, create_todo_repository

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True})


@app.get("/")
async def root():
    return RedirectResponse(app.docs_url)


@app.post("/create/{key}", status_code=HTTP_201_CREATED)
def create(key: str, value: str, todo_repository: TodoRepository = Depends(create_todo_repository)):
    with todo_repository as repo:
        repo.save(Todo(key=key, value=value))


@app.get("/get/{key}", response_model=Optional[Todo])
def get(key: str, todo_repository: TodoRepository = Depends(create_todo_repository)):
    with todo_repository as repo:
        return repo.get_by_key(key)

@app.get("/get1")
def get():
    return "hello"

@app.get("/get2")
def get():
    return "hello2"

@app.get("/get3")
def get():
    return "hello3"

@app.get("/get4")
def get():
    return "hello4"

@app.get("/get5")
def get():
    return "hello5"

@app.get("/find", response_model=List[Todo])
def find(todo_filter: TodoFilter = Depends(), todo_repository: TodoRepository = Depends(create_todo_repository)):
    with todo_repository as repo:
        return repo.get(todo_filter)
