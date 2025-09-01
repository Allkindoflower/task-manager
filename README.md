# Task Manager

A full-stack web application that gamifies task management by framing tasks as "quests." Built with FastAPI backend, SQLite database, and responsive frontend interface.

## Overview

- This is a web-app I made so users can easily set a task (quest) for themselves 
- Optionally add a deadline, then select a priority and finally Add Quest button to save it in a database.
- Users can also mark done/incomplete their tasks, or delete them if they wish.

## Why "Quest Manager"?

The "Quest Manager" will welcome you to the web page, despite the project being labeled a task manager.
I wanted a unique spin on the general "to-do" app concept, this way task setting is somewhat
gamified, increasing the possibility of a user reusing the app in the future.

## Tech stacks

- Python 3.11.x+
- FastAPI
- uvicorn
- SQLite

**Development:**
- pytest (testing)
- Docker (containerization)

## Features

- Add a task
- Optionally choose a deadline (Users are allowed to enter any strings they want for creativity)
- Toggle a task as completed or incomplete 
- Delete a task (A pop-up appears for confirmation)

## The "Quest Manager" in action

<img width="786" height="895" alt="taskmanagerscreenshot" src="https://github.com/user-attachments/assets/a9b76a62-3b5a-46f1-b87c-b29bbc6939b6" />

## How to run

-  Fork the repo via GitHubNavigate to your projects folder or its equivalent
- Clone the forked repo at https://github.com/YOUR-USERNAME/task-manager using a Git interface of your preference
(I use Git Bash: 'git clone <your forked repo link>')

- Navigate to project root
- Launch a terminal, then create & activate a Python environment 
(highly recommended, double-check that you're on the correct venv)
- Install requirements: `pip install -r requirements.txt`  
- Start server: uvicorn main:app --reload

To test endpoints via Swagger UI, navigate to: http://127.0.0.1:8000/docs

To use the app, navigate to http://127.0.0.1:8000, or the deployed live demo (You may have to wait a few seconds): https://task-manager-7jyz.onrender.com




### License
MIT © Uğur Baştuğ
