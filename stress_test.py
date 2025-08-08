import random
import string
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def task_name():
    return "do stuff"

def deadline():
    options = ["2025-12-31", "2024-01-01", "", None]
    return random.choice(options)

def random_user_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=36))

def test_task_cycle_and_stress():
    user_id = random_user_id()
    headers = {"X-User-ID": user_id}

    initial = client.get("/tasks", headers=headers)
    assert initial.status_code == 200
    assert isinstance(initial.json(), list)

    task = {"name": "initial test task", "deadline": None}
    response = client.post("/tasks", json=task, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    task_id = data["id"]


    for _ in range(200):
        t = {"name": task_name(), "deadline": deadline()}
        r = client.post("/tasks", json=t, headers=headers)
        assert r.status_code == 200
        assert "id" in r.json()


    all_tasks = client.get("/tasks", headers=headers).json()
    assert isinstance(all_tasks, list)
    assert len(all_tasks) == 200 + 1 #initial test task

    assert any(t["name"] == "initial test task" for t in all_tasks)


    toggle_res = client.patch(f"/tasks/{task_id}/toggle", headers=headers)
    assert toggle_res.status_code == 200
    assert toggle_res.json().get("message") == "Status toggled"

  
    delete_res = client.delete(f"/tasks/{task_id}", headers=headers)
    assert delete_res.status_code == 200
    assert delete_res.json().get("message") == "Task deleted"


    remaining_tasks = client.get("/tasks", headers=headers).json()
    assert not any(t["id"] == task_id for t in remaining_tasks) #confirm no task is in json file
