from pydantic import BaseModel

class Todo(BaseModel):
    id: str
    todo: str