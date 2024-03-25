#!/usr/bin/python3

"""
This script retrieves info abt employee's TODO list progress using a REST API.
It accepts an employee ID as a parameter and exports the progress of their
TODO list in both CSV and JSON formats.
"""

import csv
import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieve and export the TODO list progress in both CSV and JSON formats.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # Define the base URL of the API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Construct the URL for the employee's TODO list
    todo_url = f'{base_url}/todos?userId={employee_id}'

    # Send a GET request to the API
    response = requests.get(todo_url)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve TODO list for employee {employee_id}")
        return

    # Parse the JSON response
    todos = response.json()

    # Get the employee's name
    employee_info_url = f'{base_url}/users/{employee_id}'
    employee_info_response = requests.get(employee_info_url)
    employee_name = employee_info_response.json().get('name')

    # Export TODO list progress to CSV
    export_to_csv(employee_id, employee_name, todos)

    # Export TODO list progress to JSON
    export_to_json(employee_id, employee_name, todos)


def export_to_csv(employee_id, employee_name, todos):
    """
    Export TODO list progress to CSV.

    Args:
        employee_id (int): The ID of the employee.
        employee_name (str): The name of the employee.
        todos (list): List of TODO items.

    Returns:
        None
    """
    csv_filename = f'USER_ID.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([
            "USER_ID",
            "USERNAME",
            "TASK_COMPLETED_STATUS",
            "TASK_TITLE"
            ])
        for todo in todos:
            csv_writer.writerow([
                employee_id,
                employee_name,
                todo['completed'],
                todo['title']
                ])
    print(f"TODO list progress for {employee_name} exported to {csv_filename}")


def export_to_json(employee_id, employee_name, todos):
    """
    Export TODO list progress to JSON.

    Args:
        employee_id (int): The ID of the employee.
        employee_name (str): The name of the employee.
        todos (list): List of TODO items.

    Returns:
        None
    """
    json_data = {str(employee_id): [{
        "task": todo['title'], "completed": todo['completed'],
        "username": employee_name} for todo in todos]}
    json_filename = f'USER_ID.json'  # Correcting filename
    with open(json_filename, 'w') as jsonfile:
        json.dump(json_data, jsonfile, indent=4)
    print(f"TODO list progress {employee_name} exported to {json_filename}")


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    # Get the employee ID from command line argument
    employee_id = int(sys.argv[1])

    # Call the function to retrieve and export TODO list progress
    get_employee_todo_progress(employee_id)
