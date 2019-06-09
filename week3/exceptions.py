import os.path
import traceback

filename = 'file/not/found'

try:
    if not os.path.exists(filename):
        raise ValueError('file is not found', filename)
except ValueError as error:
    message, filename = error.args[0], error.args[1]
    print(message, filename)

try:
    with open(filename) as file:
        content = file.read()
except OSError as err:
    traceback.print_exc()

try:
    raw = input('input a number: ')
    if not raw.isdigit():
        raise ValueError('bad number', raw)
except ValueError as err:
    print(err.args[0], err.args[1])
    raise TypeError('error') from err
