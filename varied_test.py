import random
import string
import os
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

DB_PATH = "./database.db"

#------------------------------------------------------
# TEST TASK CYCLE AND STRESS
# This test checks the basic functionality of task creation, retrieval, toggling status, and deletion.
# It also stresses the system by creating a large number of tasks.
#------------------------------------------------------
def task_name():
    return "do stuff"

def deadline():
    options = ["2025-12-31", "2024-01-01", "In 2 days", None]
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

    #
    assert isinstance(task_id, int)
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

#------------------------------------------------------
# TEST TASK NAME TOO LONG
# This test checks if the API correctly handles a task name that exceeds the maximum length.
# It should return a validation error when trying to create a task with a name that is too long.
#------------------------------------------------------

def test_task_name_too_long():
    user_id = random_user_id()
    headers = {"X-User-ID": user_id}
    
    long_name = "a" * 300 
    task = {"name": long_name, "deadline": None}
    
    response = client.post("/tasks", json=task, headers=headers)
    
    # Expecting a validation error or rejection (HTTP 422 Unprocessable Entity is common)
    assert response.status_code == 422 or response.status_code == 400
    
    # Optionally check error detail for clarity
    json_response = response.json()
    assert "detail" in json_response or "error" in json_response

#------------------------------------------------------
# TEST INVALID PRIORITY
# This test checks if the API correctly handles an invalid priority value.
# It should return a validation error when trying to create a task with an invalid priority.
#------------------------------------------------------

def test_invalid_priority():
    user_id = random_user_id()
    headers = {"X-User-ID": user_id}
    invalid_task = {"name": "Test invalid priority", "deadline": None, "priority": 5}
    response = client.post("/tasks", json=invalid_task, headers=headers)
    assert response.status_code == 422


#------------------------------------------------------
# TEST USER SEPARATION
# This test ensures that tasks created by one user are not accessible by another user.
# It simulates two users creating tasks and verifies that they can only see their own tasks.
#------------------------------------------------------

def test_user_separation():
    user_a = "user_a_id"
    user_b = "user_b_id"

    # User A creates a task
    res_a_post = client.post(
        "/tasks",
        headers={"X-User-ID": user_a},
        json={"name": "User A Task", "deadline": "randomassday", "priority": 2}
    )
    assert res_a_post.status_code == 200
    task_a_id = res_a_post.json()["id"]

    # User B creates a task
    res_b_post = client.post(
        "/tasks",
        headers={"X-User-ID": user_b},
        json={"name": "User B Task", "deadline": "infinite", "priority": 3}
    )
    assert res_b_post.status_code == 200
    task_b_id = res_b_post.json()["id"]

    # User A fetches tasks — should only get their own
    res_a_get = client.get("/tasks", headers={"X-User-ID": user_a})
    assert res_a_get.status_code == 200
    tasks_a = res_a_get.json()
    assert any(t["id"] == task_a_id for t in tasks_a)
    assert all(t["name"] != "User B Task" for t in tasks_a)

    # User B fetches tasks — should only get their own
    res_b_get = client.get("/tasks", headers={"X-User-ID": user_b})
    assert res_b_get.status_code == 200
    tasks_b = res_b_get.json()
    assert any(t["id"] == task_b_id for t in tasks_b)
    assert all(t["name"] != "User A Task" for t in tasks_b)

def test_db_persistence():
    # Remove old DB to start fresh
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    # Step 1: Create a task
    task = {"name": "Persistent task", "deadline": None}
    response = client.post("/tasks", json=task, headers={"X-User-ID": "user_test"})
    assert response.status_code == 200
    task_id = response.json()["id"]

    # Step 2: Simulate app restart by re-importing TestClient
    # this would be a container restart
    client2 = TestClient(app)

    # Step 3: Fetch tasks again
    tasks = client2.get("/tasks", headers={"X-User-ID": "user_test"}).json()

    # Assert that our task still exists
    assert any(t["id"] == task_id for t in tasks), "Task not persisted!"