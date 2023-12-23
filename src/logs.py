import json


LOG_FILE = 'log.json'


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


def save_log(filepath, log):
    data = load_items(filepath)

    logs = get_current_log(filepath)

    if list(log) not in logs:
        logs.append(log)






def get_current_log(filepath):
    data = load_items(filepath)

    key_list = list(data.keys())
    last_log_key = key_list[-1]

    return data[last_log_key]













