#!/usr/bin/python3
"""
Import modules
"""
import csv
import json
import requests
from sys import argv


def export():
    """
    Return API data
    """
    USERS = []
    userss = requests.get("http://jsonplaceholder.typicode.com/users")
    for u in userss.json():
        USERS.append((u.get('id'), u.get('username')))
    TASK_STATUS_TITLE = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for t in todos.json():
        TASK_STATUS_TITLE.append((t.get('userId'),
                                  t.get('completed'),
                                  t.get('title')))

    """
    Export to json
    """
    data = dict()
    for u in USERS:
        t = []
        for task in TASK_STATUS_TITLE:
            if task[0] == u[0]:
                t.append({"task": task[2], "completed": task[1],
                          "username": u[1]})
        data[str(u[0])] = t
    filename = "todo_all_employees.json"
    with open(filename, "w") as f:
        json.dump(data, f, sort_keys=True)


if __name__ == "__main__":
    export()
