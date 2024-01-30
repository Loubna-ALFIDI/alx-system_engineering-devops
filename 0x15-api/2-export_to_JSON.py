#!/usr/bin/python3
""" Export to CSV """


import json
import requests
import sys


if __name__ == "__main__":
    """ Gather data from an API"""
    id_user = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/'
    userid = f'users?id={id_user}'
    user_response = requests.get(f'{url}{userid}')
    user = user_response.json()
    todos = f'todos?userId={id_user}'
    done = f'{todos}&completed=true'
    todo_response = requests.get(f'{url}{todos}')
    todo = todo_response.json()
    Name = user[0].get("name")
    userName = user[0].get("username")  # Corrected line
    todosdone = requests.get(f'{url}{done}').json()
    todos_completed = len(todosdone)
    totaldone = len(todo)

    with open(f'{id_user}.json', 'w') as f:
        for todo_item in todo:
            data = f'"{id_user}","{userName}","{todo_item.get("completed")}",'
            data2 = f'"{todo_item.get("title")}"\n'
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
