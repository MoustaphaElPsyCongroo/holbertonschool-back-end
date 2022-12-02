#!/usr/bin/python3
from sys import argv
import requests

if len(argv) >= 2:
    employee_id = argv[1]

if employee_id is None:
    exit()

userId = {'userId': employee_id}
id = {'id': employee_id}
todos = requests.get(
    'https://jsonplaceholder.typicode.com/todos', params=userId)
todos = todos.json()

users = requests.get(
    'https://jsonplaceholder.typicode.com/users', params=id)
users = users.json()

employee_name = users[0].get('name')

tasks_done = [d for d in todos if d.get('completed') is True]
tasks_done_nb = len(tasks_done)
tasks_total = len(todos)


print('Employee {} is done with tasks({}/{}):'.format(employee_name,
      tasks_done_nb, tasks_total))

for task in tasks_done:
    print('\t {}'.format(task.get('title')))
