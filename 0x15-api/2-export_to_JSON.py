#!/usr/bin/python3
""" Export to CSV """


import json
import requests
import sys


if __name__ == "__main__":
    """ Gather data from an API"""
    id_user = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    userid = f'users?id={id_user}'
    user_response = requests.get(f'{url}{userid}')
    user = user_response.json()
    todos = f'todos?userId={id_user}'
    done = f'{todos}&completed=true'
    todo_response = requests.get(f'{url}{todos}')
    todo = todo_response.json()
    userName = user[0].get("username")

    with open(f'{id_user}.csv', 'w') as f:
        for todo in todo:
            data = f'"{id_user}","{userName}","{todo.get("completed")}",'
            data2 = f'"{todo.get("title")}"\n'
            f.write(data+data2)

    tasks = []
    for todo_item in todo:
        task_info = {
            "task": todo_item.get("title"),
            "completed": todo_item.get("completed"),
            "username": userName
        }
        tasks.append(task_info)

    json_data = {id_user: tasks}
    with open(f'{id_user}.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=4)
