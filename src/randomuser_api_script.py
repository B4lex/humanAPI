from database import db_manager
import requests


URL = 'https://randomuser.me/api/'
HUMANS_COUNT = 100


def fetch_and_save_humans_data():
    response = requests.get(
        URL,
        params={'gender': 'male',
                'results': HUMANS_COUNT},
        headers={'User-Agent': 'humanAPI script v1'}
    )
    humans_json = response.json()
    humans_raw_data = humans_json['results']
    humans_prepared_data = list(map(get_prepared_data, humans_raw_data))
    for human_data in humans_prepared_data:
        db_manager.insert_data(human_data)


def get_prepared_data(human_dict):
    """
    Returns data ready to saving into database
    """
    full_name = ' '.join(
        [name_pattern for name_pattern in human_dict['name'].values()]
    )
    return {
        'full_name': full_name,
        'gender': human_dict['gender'],
        'email': human_dict['email'],
        'phone': human_dict['phone'],
        'cell': human_dict['cell'],
        'picture_url': human_dict['picture']['medium'],
        'nationality': human_dict['nat']
}


if __name__ == '__main__':
    fetch_and_save_humans_data()
