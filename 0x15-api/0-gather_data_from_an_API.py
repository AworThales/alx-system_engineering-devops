#!/usr/bin/python3
'''this is a script that gathers data from an API.
'''
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
            user_name = user_response.get('name')
            todos = list(filter(lambda x: x.get('userId') == id, todos_response))
            todos_done = list(filter(lambda x: x.get('completed'), todos))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    user_name,
                    len(todos_done),
                    len(todos)
                )
            )
            for todo_done in todos_done:
                print('\t {}'.format(todo_done.get('title')))
