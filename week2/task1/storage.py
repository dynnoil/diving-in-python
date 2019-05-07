import os
import json
import tempfile
import argparse

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if not os.path.exists(storage_path):
    open(storage_path, 'w').close()


def read_storage():
    with open(storage_path, 'r') as file:
        raw_data = file.read()
        if raw_data:
            return json.loads(raw_data)

        return {}


def put(key, value):
    storage = read_storage()
    if key not in storage:
        storage[key] = []

    storage[key].append(value)

    with open(storage_path, 'w') as file:
        file.write(json.dumps(storage))


def get(key):
    storage = read_storage()
    return storage.get(key)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='a key for a storable data')
    parser.add_argument('--val', help='a value for a storable data')
    args = parser.parse_args()

    key = args.key
    value = args.val

    if key and value:
        put(key, value)
    elif key:
        values = get(key)
        print(', '.join(values) if values else '')
    else:
        print('Wrong command')
