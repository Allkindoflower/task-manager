Task Manager App
This is a simple task manager application built with FastAPI and SQLite. It lets you create, view, complete, and delete tasks with deadlines, all through a clean web interface. The project started as a CLI app and evolved into a full web app — a nice way to practice building backend APIs and connecting them with a frontend.

Features
Add tasks with optional deadlines

Mark tasks as done or incomplete

Delete tasks you no longer need

Tasks are saved in an SQLite database

Simple and clean UI with responsive buttons

Status indicators in green (Done) and red (Incomplete)

Modern black and gold theme for a sleek look

How to Use
Run the FastAPI backend (main.py) — it handles all database interactions and serves the API.

Open the frontend in your browser (served from the static folder).

Add tasks, mark them complete/incomplete, or delete them right from the interface.

The task list updates instantly after every change.

Tech Stack
Python 3 with FastAPI (backend API)

SQLite (simple, file-based database)

Vanilla JavaScript for frontend interactions

HTML & CSS with a black/gold color scheme

Jinja2 only if you want to serve templates dynamically (optional)

Why This Project?
I built this to sharpen my skills building full-stack apps and practice clean API design. It’s also a stepping stone to more complex projects involving user management, authentication, and personalized data. It started as a CLI project, then transitioned to a modern web app — so I got to learn both paradigms.

How I Built It
Started with a simple CLI app managing tasks locally with SQLite

Refactored database code to be reusable by FastAPI routes

Built RESTful API endpoints to add/view/delete/toggle tasks

Created a responsive frontend that talks to the API with fetch requests

Styled the interface with a consistent black and gold theme for readability and mood

What’s Next?
Add user authentication to separate data per user

Improve error handling and input validation

Deploy it so it can be accessed anywhere

Add filtering and sorting options

How to Run Locally
Clone the repo

Create a virtual environment and install dependencies (FastAPI, uvicorn)

Run python main.py to start the backend server

Open your browser to http://localhost:8000

Enjoy managing your tasks
