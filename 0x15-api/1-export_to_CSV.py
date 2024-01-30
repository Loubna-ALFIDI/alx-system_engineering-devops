#!/usr/bin/python3
""" Export to CSV """


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
    todosdone = requests.get(f'{url}{done}').json()
    todos_completed = len(todosdone)
    totaldone = len(todo)
    userName = user[0].get("username")

    with open(f'{id_user}.csv', 'w') as f:
        for todo in todo:
            data = f'"{id_user}","{userName}","{todo.get("completed")}",'
            data2 = f'"{todo.get("title")}"\n'
            f.write(data+data2)
