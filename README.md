# Task Manager

Add tasks with deadlines and priority. Mark done or delete.

## How to run

1. Clone repo  
2. Create & activate Python venv  
3. Install requirements: `pip install -r requirements.txt`  

Start server: uvicorn main:app --reload

Open browser: http://localhost:8000

Features
Add task name + optional deadline

Select priority (Low, Medium, High)

Toggle done/undone

Delete task

User tasks saved by browser ID

Data stored in SQLite

License
MIT © Uğur Baştuğ
