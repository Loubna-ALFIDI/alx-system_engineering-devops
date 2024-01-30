#!/usr/bin/python3
""" Export to JSON for all employees """

import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    users_response = requests.get(url + 'users')
    users = users_response.json()

    all_tasks = {}

    for user in users:
        user_id = str(user['id'])
        username = user['username']

        todos_response = requests.get(url + f'todos?userId={user_id}')
        todos = todos_response.json()

        tasks = []
        for todo in todos:
            task_info = {
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]
            }
            tasks.append(task_info)

        all_tasks[user_id] = tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file, indent=4)
