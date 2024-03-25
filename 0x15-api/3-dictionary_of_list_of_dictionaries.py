#!/usr/bin/python3

"""
This script retrieves information about employees' TODO list progress
It exports the progress of their TODO lists for all employees in JSON format.
"""

import json
import requests
import sys


def get_all_employees_todo_progress():
    """
    Retrieve and export the TODO list progress of all employees in JSON format

    Returns:
        None
    """
    # Define the base URL of the API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Send a GET request to retrieve all users
    users_url = f'{base_url}/users'
    users_response = requests.get(users_url)

    # Check if the request was successful
    if users_response.status_code != 200:
        print("Failed to retrieve user information")
        return

    # Parse the JSON response to get list of users
    users = users_response.json()

    # Create a dictionary to store todo progress for all employees
    all_employees_todo_progress = {}

    # Iterate over each user to fetch their todo progress
    for user in users:
        user_id = user['id']
        username = user['username']

        # Construct URL for user's TODO list
        todo_url = f'{base_url}/todos?userId={user_id}'

        # Send a GET request to retrieve user's todo list
        todo_response = requests.get(todo_url)

        # Check if the request was successful
        if todo_response.status_code != 200:
            print(f"Failed to retrieve TODO list for user {user_id}")
            continue

        # Parse the JSON response to get user's todo list
        todos = todo_response.json()

        # Store todo progress for the user
        user_todo_progress = []
        for todo in todos:
            task_title = todo['title']
            task_completed = todo['completed']
            user_todo_progress.append({
                "username": username,
                "task": task_title,
                "completed": task_completed
                })

        all_employees_todo_progress[user_id] = user_todo_progress

    # Export todo progress of all employees to JSON file
    json_filename = 'todo_all_employees.json'
    with open(json_filename, 'w') as jsonfile:
        json.dump(all_employees_todo_progress, jsonfile, indent=4)

    print(f"TODO list progress for all employees exported to {json_filename}")


if __name__ == "__main__":
    # Call the function to retrieve and export TODO list progress for employee
    get_all_employees_todo_progress()
