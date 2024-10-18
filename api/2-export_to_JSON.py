#!/usr/bin/python3
"""Script to export employee TODO list data in JSON format"""

import json
import requests
import sys


def export_to_json(employee_id):
    """Export TODO list data for a given employee ID to a JSON file."""
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )

    user_info = requests.get(url).json()
    todo_info = requests.get(todo_url).json()

    username = user_info.get("username")

    # Prepare data for JSON
    tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        for task in todo_info
    ]

    data = {str(employee_id): tasks}

    # File name format: USER_ID.json
    file_name = f"{employee_id}.json"

    # Write to JSON
    with open(file_name, mode='w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_to_json(employee_id)
    except ValueError:
        print("Please provide a valid integer for the employee ID.")
        sys.exit(1)
