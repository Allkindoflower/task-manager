from fastapi import FastAPI, Header
from typing import Optional
from pydantic import BaseModel
from database import get_tasks_db, add_task_db, delete_task_db, toggle_task_status_db
from fastapi.staticfiles import StaticFiles


app = FastAPI()


class Task(BaseModel):
    id: int
    name: str
    deadline: Optional[str] = None
    status: bool = False

class AddedTask(BaseModel):
    name: str
    deadline: Optional[str] = None
    status: bool = False


@app.get("/tasks")
def read_tasks(user_id: str = Header(..., alias="X-User-ID")):
    tasks = get_tasks_db(user_id)
    return [dict(task) for task in tasks]

@app.post("/tasks")
def create_task(task: AddedTask):
    task_id = add_task_db(task.name, task.deadline)
    return {"id": task_id, "name": task.name, "deadline": task.deadline, "status": task.status}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    success = delete_task_db(task_id)
    if success:
        return {"message": "Task deleted"}
    return {"error": "Task not found"}

@app.patch("/tasks/{task_id}/toggle")
def toggle_task_status(task_id: int):
    success = toggle_task_status_db(task_id)
    if success:
        return {"message": "Status toggled"}
    return {"error": "Task not found"}


app.mount("/", StaticFiles(directory="static", html=True), name="static")
