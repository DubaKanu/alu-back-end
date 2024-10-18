#!/usr/bin/python3
"""Script to export all employee TODO list data in JSON format"""

import json
import requests


def export_all_to_json():
    """Export all TODO list data for all employees to a JSON file."""
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    data = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        tasks = [
            {
                "username": username,
                "task": todo.get("title"),
                "completed": todo.get("completed")
            }
            for todo in todos if todo.get("userId") == user_id
        ]
        data[str(user_id)] = tasks

    # File name: todo_all_employees.json
    file_name = "todo_all_employees.json"

    # Write to JSON
    with open(file_name, mode='w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    export_all_to_json()
