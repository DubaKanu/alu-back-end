#!/usr/bin/python3
"""Script to gather data from an API"""

import requests
import sys


def gather_data(employee_id):
    """Gather TODO list data for a given employee ID."""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    user_info = requests.get(user_url).json()
    todo_info = requests.get(todo_url).json()

    completed_tasks = [task for task in todo_info if task.get("completed")]

    print(
        f"Employee {user_info.get('name')} is done with "
        f"{len(completed_tasks)}/{len(todo_info)} tasks:"
    )
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        gather_data(employee_id)
    except ValueError:
        print("Please provide a valid integer for the employee ID.")
        sys.exit(1)
