import argparse
import json
import os
from datetime import datetime

# Path to store the tasks in a JSON file
TASKS_FILE = "tasks.json"

# Function to load tasks from JSON file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def generate_id(tasks):

    return max([task['id'] for task in tasks], default=0) + 1

def handle_args():
    parser = argparse.ArgumentParser(description='Task tracker CLI')
    subparsers = parser.add_subparsers(dest='command')

    parser_add = subparsers.add_parser('add', help='Add a new task')
    parser_add.add_argument('description', type=str, help='Task description')

    parser_update = subparsers.add_parser('update', help='Update an existing task')
    parser_update.add_argument('id', type=int, help='ID of the task to update')
    parser_update.add_argument('description', type=str, help='New task description')

    parser_delete = subparsers.add_parser('delete', help='Delete a task')
    parser_delete.add_argument('id', type=int, help='ID of the task to delete')

    parser_mark = subparsers.add_parser('mark', help='Mark a task')
    parser_mark.add_argument('status', choices=['in-progress', 'done'], help='Mark the task status')
    parser_mark.add_argument('id', type=int, help='ID of the task to mark')

    parser_list = subparsers.add_parser('list', help='List tasks')
    parser_list.add_argument('status', nargs='?', choices=['all', 'done', 'todo', 'in-progress',], default='all', help='List tasks by status')

    return parser.parse_args()

def add_task(description):
    tasks = load_tasks()
    task_id = generate_id(tasks)
    task = {
        'id' : task_id,
        'description' : description,
        'status': 'todo',
        'createdAt' : datetime.now().isoformat(),
        'updatedAt' : datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")

def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully")
            return
    print(f"Task with ID {task_id} not found")

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f"Task {task_id} deleted successfully")

def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}")
            return
    print(f"Task with ID {task_id} not found")

def list_tasks(status):
    tasks = load_tasks()
    if status == 'all':
        filtered_tasks = tasks
    else:
        filtered_tasks = [task for task in tasks if task['status'] == status]

    if not filtered_tasks:
        print(f"no tasks found with status '{status}'")
        return

    for task in filtered_tasks:
        print(f"[{task['id']}] {task['description']} (Status: {task['status']})")

def main():
    args = handle_args()

    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'update':
        update_task(args.id, args.description)
    elif args.command == 'delete':
        delete_task(args.id)
    elif args.command == 'mark':
        mark_task(args.id, args.status)
    elif args.command == 'list':
        list_tasks(args.status)
    else:
        print('Invalid command. Use --help for usage instructions.')

if __name__ == '__main__':
    main()

"""Instructions

To add a task -- python task_tracker.py add "Buy groceries" 
To update a task -- python task_tracker.py update 1 "Buy groceries and cook dinner"
To delete a task -- python task_tracker.py delete 1
To mark a task  as in-progress -- python task_tracker.py mark in-progress 1
To mark a task as done -- python task_tracker.py mark done 1
To show the lists of tasks -- 
python task_tracker.py list
python task_tracker.py list done
python task_tracker.py list todo
python task_tracker.py list in-progress

notes: the numbers used to update or delete or mark, are the tasks ID.
When tasks are added, it'll auto assign as todo.

"""    