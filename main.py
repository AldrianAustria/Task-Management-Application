import pymysql
from pymysql.connections import Connection as MySQLConnection
import os
import configparser
from datetime import datetime
import tasks

# Database configuration and connection setup
config = configparser.ConfigParser()
config_file_path = config_file_path = os.path.join(os.getcwd(), 'db_access.cfg')
file_read = config.read(config_file_path)

db = MySQLConnection(
    host = config['database']['host'],
    user = config['database']['user'],
    password = config['database']['password'],
    database = config['database']['database'],
    port = int(config['database']['port'])
)

conn = tasks.Tasks(db)

PRIORITY_LEVELS = ['Low', 'Medium', 'High']
STATUS_OPTIONS = ['Pending', 'In Progress', 'Completed']

while True:
    print("1. Create Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date_str = input("Enter due date (YYYY-MM-DD): ")
            if due_date_str.strip():
                try:
                    due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
                except ValueError:
                    print("Invalid date entered, leaving due date blank.")
                    due_date = None
            else:
                due_date = None
            priority = input("Enter task priority (Low, Medium, High): ")
            if priority not in PRIORITY_LEVELS:
                print("Invalid priority entered, defaulting to 'Low'.")
                priority = 'Low'
            status = input("Enter task status (Pending, In Progress, Completed): ")
            if status not in STATUS_OPTIONS:
                print("Invalid status entered, defaulting to 'Pending'.")
                status = 'Pending'
            conn.create_task(title, description, due_date, priority, status, datetime.now())
            print("Task created successfully!")
        case '2':
            tasks_data = conn.get_tasks()
            for task in tasks_data:
                print(f"ID: {task[0]}, Title: {task[1]}, Description: {task[2]}, Due: {task[3].date() if task[3] else 'None'}, Priority: {task[4]}, Status: {task[5]}, Created At: {task[6]}")
        case '3':
            task_id = input("Enter task ID to update: ")
            tasks_data = conn.get_tasks()
            task_ids = [task[0] for task in tasks_data]
            if not task_id.isdigit() or int(task_id) <= 0 or int(task_id) not in task_ids:
                print("Invalid task ID entered.")
                continue
            title = input("Enter new title (leave blank to keep current): ")
            description = input("Enter new description (leave blank to keep current): ")
            priority = input("Enter new priority (Low, Medium, High) (leave blank to keep current): ")
            if priority and priority not in PRIORITY_LEVELS:
                print("Invalid priority entered, keeping current value.")
                priority = None
            status = input("Enter new status (Pending, In Progress, Completed) (leave blank to keep current): ")
            if status and status not in STATUS_OPTIONS:
                print("Invalid status entered, keeping current value.")
                status = None
            conn.update_task(task_id, title if title.strip() else None, description if description.strip() else None, priority, status)
            print("Task updated successfully!")
        case '4':
            task_id = input("Enter task ID to delete: ")
            tasks_data = conn.get_tasks()
            task_ids = [task[0] for task in tasks_data]
            if not task_id.isdigit() or int(task_id) <= 0 or int(task_id) not in task_ids:
                print("Invalid task ID entered.")
                continue
            conn.delete_task(task_id)
            print("Task deleted successfully!")
        case '5':
            print("Exiting...")
            break