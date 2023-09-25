#!/usr/bin/python3
'''A script that gathers data from an API and exports it to a JSON file.
'''
import json
import requests

B_URL = 'https://jsonplaceholder.typicode.com'
'''The API's URL.'''

if __name__ == '__main__':
    users_response = requests.get('{}/users'.format(B_URL)).json()
    todos_response = requests.get('{}/todos'.format(B_URL)).json()
    users_data = {}
    for user in users_response:
        id = user.get('id')
        username = user.get('username')
        todos = list(filter(lambda x: x.get('userId') == id, todos_response))
        user_data = list(map(
            lambda x: {
                'username': username,
                'task': x.get('title'),
                'completed': x.get('completed')
            },
            todos
        ))
        users_data['{}'.format(id)] = user_data
    with open('todo_all_employees.json', 'w') as file:
        json.dump(users_data, file)
