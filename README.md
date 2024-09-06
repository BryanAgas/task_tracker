# Task Tracker CLI Application

A simple command-line interface (CLI) application for tracking tasks with priorities and statuses. You can add, update, delete, mark, and list tasks. Tasks are stored in a JSON file for persistence.

## Features

- Add tasks with priorities (Top, Mid, Low)
- Update tasks by ID
- Delete tasks by ID
- Mark tasks as `in-progress` or `done`
- List tasks by status (all, done, todo, in-progress)
- Tasks are stored in `tasks.json`

# Usage
## 1. Add a New Task
Add a task by providing a description and priority

python task_tracker.py add "Task description" [priority]

[priority]: Choose from 1 (Top), 2 (Mid), or 3 (Low)

Example: 
python task_tracker.py add "Finish project report" 1

## 2. Update an Existing Task
Update a task's description and priority using its ID:

python task_tracker.py update [id] "New task description" [priority]

[id]: The task ID you want to update
[priority]: Choose from 1 (Top), 2 (Mid), or 3 (Low)

Example:
python task_tracker.py update 1 "Review project report" 2

## 3. Delete a Task
Delete a task by its ID:

python task_tracker.py delete [id]

[id]: The task ID you want to delete

Example:
python task_tracker.py delete 1

## 4. Mark a Task's Status
Mark a task as in-progress or done using its ID:

python task_tracker.py mark [id] [status]

[id]: The task ID you want to mark
[status]: Choose from in-progress or done

Example:
python task_tracker.py mark 1 in-progress

## 5. List Tasks
You can list tasks based on their status.

python task_tracker.py list [status]

[status]: Choose from all, done, todo, or in-progress

Examples:

### List all tasks:
python task_tracker.py list all
### List tasks with status done:
python task_tracker.py list done
### List tasks with status in-progress:
python task_tracker.py list in-progress
### List tasks with status todo:
python task_tracker.py list todo

## 6. Help Command
If you need help or want to see the usage of commands:

python task_tracker.py --help



























































