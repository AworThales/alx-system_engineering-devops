#!/usr/bin/python3
'''This is a script that gathers data from an API and exports it to a JSON file.
'''
import json
import re
import requests
import sys

B_URL = 'https://jsonplaceholder.typicode.com'
'''The API's URL.'''

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user_response = requests.get('{}/users/{}'.format(B_URL, id)).json()
            todos_response = requests.get('{}/todos'.format(B_URL)).json()
            username = user_response.get('username')
            todos = list(filter(lambda x: x.get('userId') == id, todos_response))
            with open('{}.json'.format(id), 'w') as file:
                user_data = list(map(
                    lambda x: {
                        'task': x.get('title'),
                        'completed': x.get('completed'),
                        'username': username
                    },
                    todos
                ))
                users_data = {
                    '{}'.format(id): user_data
                }
                json.dump(users_data, file)
