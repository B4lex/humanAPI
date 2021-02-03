import requests


URL = 'https://randomuser.me/api/'


def get_users_list():
    response = requests.get(
        URL,
        params={'gender': 'male',
                'results': 100},
        headers={'User-Agent': 'humanAPI script v1'}
    )
    users_json = response.json()
    return users_json['results']
