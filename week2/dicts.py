from collections import OrderedDict

empty_dict = {}
empty_dict = dict()

collections_map = {
    'mutable': ['list', 'dict', 'set'],
    'immutable': ['tuple', 'frozenset']
}

print(collections_map['mutable'])

try:
    print(collections_map['some_key'])
except KeyError as error:
    print(error)
finally:
    print('Its Ok, go futher!')

print(collections_map.get('some_key'), 'default_value')

assert 'mutable' in collections_map

unknown_dict = {}
print(unknown_dict.setdefault('key', 'value'))

for key in collections_map:
    print(f"Key: {key}")

for key, value in collections_map.items():
    print(f"{key}: {value}")

for value in collections_map.values():
    print(f"Value: {value}")

ordered = OrderedDict()

for number in range(10):
    ordered[number] = str(number)

print(ordered)