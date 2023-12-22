import json


LOGS = 'logs.json'


def save_items(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(f, data)


def load_items(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    return data















