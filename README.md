# Task Manager

A simple task manager web app built with FastAPI, SQLite, and vanilla JavaScript.  
Quickly add tasks with deadlines and priorities, mark them done, or delete — all in one place.

---

## Features

- Add tasks with optional deadlines  
- Set task priority (Low, Medium, High) via an intuitive toggle UI  
- Mark tasks as complete or incomplete  
- Delete tasks  
- Tasks are stored per user using localStorage-based user ID  
- Persistent storage with SQLite database  
- Responsive and clean UI with dark theme  


---

## Getting Started

### Prerequisites

- Python 3.8+  
- pip package manager

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/task-manager.git
   cd task-manager
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
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
Running the App
Start the FastAPI server:

bash
Copy
Edit
uvicorn main:app --reload
Open your browser and go to http://localhost:8000

Project Structure
graphql
Copy
Edit
.
├── main.py           # FastAPI app and routes
├── database.py       # SQLite database access and schema
├── models.py         # Pydantic models
├── static/
│   ├── index.html    # Frontend HTML
│   ├── script.js     # Frontend JS
│   └── style.css     # CSS styles
├── requirements.txt  # Python dependencies
└── README.md         # This file
Usage
Enter a task name

(Optional) Enter a deadline

Select a priority by clicking one of the priority boxes (Low / Medium / High)

Click Add Task

Tasks appear in the list with colored priority labels

Use Done/Incomplete button to toggle status

Use Delete button to remove a task

Notes
Tasks are associated with a user ID stored in the browser’s localStorage

The app is a prototype and does not implement authentication

All data is stored locally on the server in a SQLite database

License
MIT License © Uğur Baştuğ
