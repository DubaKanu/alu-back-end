#!/usr/bin/python3
"""Script to export employee TODO list data in CSV format"""

import csv
import requests
import sys


def export_to_csv(employee_id):
    """Export TODO list data for a given employee ID to a CSV file."""
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )

    user_info = requests.get(url).json()
    todo_info = requests.get(todo_url).json()

    username = user_info.get("username")

    # File name format: USER_ID.csv
    file_name = f"{employee_id}.csv"

    # Write to CSV
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todo_info:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_to_csv(employee_id)
    except ValueError:
        print("Please provide a valid integer for the employee ID.")
        sys.exit(1)
