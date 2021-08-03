from model import Todo
from db import(
    fetchOneTodo,
    fetchTodos,
    createTodo,
    updateTodo,
    removeTodo
)
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


origins = ["https://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def root():
    return ("helo again xiscode")


@app.get("/todo")
async def getTodo():
    response = await fetchTodos()
    return response


@app.get("/todo/{id}", response_model=Todo)
async def getoneTodo(id):
    response = await fetchOneTodo
    if response:
        return response
    raise HTTPException(404, f"no item with id {id}")


@app.post("/todo", response_model=Todo)
async def postTodo(todo: Todo):
    response = await createTodo(todo.dict())
    return response
    # if response:
    #     return response
    # raise HTTPException(400, "Something went wrong/Bad request")


@app.put("/todo/{id}", response_model=Todo)
async def updateTodo(id: str, todo: str):
    response = await updateTodo(id, todo)
    if response:
        return response
    raise HTTPException(404, f"no item with id {id}")


@app.delete("/todo/{id}")
async def delTodo():
    response = await removeTodo(id)
    if response:
        return "successfully deleted todo"
    raise HTTPException(404, f"no item with id {id}")
