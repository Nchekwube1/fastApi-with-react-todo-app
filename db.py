from model import Todo

import motor.motor_asyncio
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")

database = client.fastApiTodo
collection = database.todo


async def fetchOneTodo(id):
    document = await collection.find_one({id: id})
    return document


async def fetchTodos():
    todos = []
    cursor = collection.find({})
    async for d in cursor:
        todos.append(Todo(**d))
    return todos


async def createTodo(todo):
    document = todo
    result = await collection.insert_one(document)
    return result


async def updateTodo(id, todo):
    await collection.update_one({"id": id}, {"$set": {
        "todo": todo
    }})
    doc = await collection.find_one({"todo": todo})
    return doc


async def removeTodo(id):
    await collection.delete_one({"id": id})
    return "Deleted successfully"
