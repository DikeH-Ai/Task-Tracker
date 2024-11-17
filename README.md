# Task Tracker: 
https://roadmap.sh/projects/task-tracker

Task Tracker is a simple command-line interface (CLI) application that helps you track and manage tasks.
## Features
- Add, update, and delete tasks
- Mark tasks as "In Progress" or "Done"
- List all tasks
- Filter tasks by status: done, not done, in progress

## How to Run

1. **Clone the repository**:
   git clone https://github.com/DikeH-Ai/Python-projects.git
   
   cd Python-projects/

2. **Make the script executable**:
    chmod +x task-tracker.py

3. **Run the task tracker**:
    ./task-tracker --help

4. **Add a Task**:
    ./task-tracker add "Buy groceries"

5. **Update a Task**:
    ./task-tracker update 1 "Finish Python project"

6. **Delete a Task**:
    ./task-tracker delete 1

7. **List All Tasks**:
    ./task-tracker list --all

8. **List Completed Tasks**:
    ./task-tracker list --done
