from fastapi import FastAPI, Header, HTTPException
from database import get_tasks_db, add_task_db, delete_task_db, toggle_task_status_db
from fastapi.staticfiles import StaticFiles
from models import AddedTask, Priority

app = FastAPI()



@app.get("/tasks")
def read_tasks(user_id: str = Header(..., alias="X-User-ID")):
    tasks = get_tasks_db(user_id)
    return [dict(task) for task in tasks]

@app.post("/tasks")
def create_task(task: AddedTask, user_id: str = Header(..., alias="X-User-ID")):
    task_id = add_task_db(task.name, task.deadline, user_id, task.priority)
    return {"id": task_id, "name": task.name, "deadline": task.deadline, "status": False, "priority": task.priority}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, user_id: str = Header(..., alias="X-User-ID")):
    success = delete_task_db(task_id, user_id)
    if success:
        return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")

@app.patch("/tasks/{task_id}/toggle")
def toggle_task_status(task_id: int, user_id: str = Header(..., alias="X-User-ID")):
    success = toggle_task_status_db(task_id, user_id)
    if success:
        return {"message": "Status toggled"}
    raise HTTPException(status_code=404, detail="Task not found")

app.mount("/", StaticFiles(directory="static", html=True), name="static")
