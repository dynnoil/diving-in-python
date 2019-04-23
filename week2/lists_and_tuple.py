import random

# Lists

empty_list = []
empty_list = list()

none_list = [None] * 8

collections = ['list', 'tuple', 'dict', 'set']

assert len(none_list) == 8

assert 'set' in collections

for collection in collections:
    print(f"Learning {collection}")

for index, collection in enumerate(collections):
    print(f"#{index}: {collection}")

# print(dir(collections))

# sorting

random_numbers = []

for _ in range(10):
    random_numbers.append(random.randint(1, 100))

print(f"Unsorted: {random_numbers}")

sorted_numbers = sorted(random_numbers)
print(f"Sorted: {sorted_numbers}")

reversed_numbers = sorted(random_numbers, reverse=True)
print(f"Reversed sort: {reversed_numbers}")

# Tuples

empty_tuple = ()
empty_tuple = tuple()

immutable_numbers = (10, 100, 1000)

try:
    immutable_numbers[0] = 0
except TypeError as error:
    print(error)
finally:
    print("It's ok, go futher!")

