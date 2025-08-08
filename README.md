# Task Manager

A simple web app to add tasks with deadlines and priorities, mark them done, or delete them.  
Built with FastAPI, SQLite, and vanilla JavaScript.

---

## Features

- Add tasks with optional deadlines  
- Choose priority (Low, Medium, High) before adding  
- Mark tasks complete/incomplete  
- Delete tasks  
- User-specific tasks saved via browser localStorage ID  
- Data stored in SQLite database  

---

## Setup

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/task-manager.git
   cd task-manager
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Initialize the database:

bash
Copy
Edit
python
>>> from database import create_table
>>> create_table()
>>> exit()
Run the app:

bash
Copy
Edit
uvicorn main:app --reload
Open http://localhost:8000 in your browser.

Usage
Enter task name and deadline (optional)

Select priority by clicking one of the boxes (default is Medium)

Click Add Task

Manage tasks in the list: toggle done, delete

License
MIT © Uğur Baştuğ
