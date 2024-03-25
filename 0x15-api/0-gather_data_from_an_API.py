#!/usr/bin/python3

"""
This script retrieves information about an employee's TODO list progress
It accepts an employee ID as a parameter and displays the progress
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieve and display the TODO list progress of an employee.

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

    # Calculate the number of completed tasks
    completed_tasks = [todo for todo in todos if todo.get('completed')]
    num_completed_tasks = len(completed_tasks)

    # Calculate the total number of tasks
    total_tasks = len(todos)

    # Get the employee's name
    employee_info_url = f'{base_url}/users/{employee_id}'
    employee_info_response = requests.get(employee_info_url)
    employee_name = employee_info_response.json().get('name')

    # Display the employee's TODO list progress
    print(f"Employee {employee_name} ({num_completed_tasks}/{total_tasks}):")
    for todo in completed_tasks:
        print(f"\t{todo.get('title')}")


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    # Get the employee ID from command line argument
    employee_id = int(sys.argv[1])

    # Call the function to retrieve and display TODO list progress
    get_employee_todo_progress(employee_id)
