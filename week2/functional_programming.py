
from functools import reduce, partial


def get_multiplier(number):
    def inner(a):
        return a * number
    return inner


multiplier = get_multiplier(10)

assert 20 == multiplier(2)


def squrify(a):
    return a ** 2


assert [0, 1, 4, 9, 16] == list(map(squrify, range(5)))

assert [0, 1, 4, 9, 16] == list(map(lambda x: x ** 2, range(5)))


def is_positive(a):
    return a > 0


assert [1, 2] == list(filter(is_positive, range(-2, 3)))

assert [1, 2] == list(filter(lambda x: x > 0, range(-2, 3)))


def stringify(l: list):
    return list(map(str, l))


assert ['1', '2', '3'] == stringify([1, 2, 3])


def multiply(a, b):
    return a * b


assert reduce(multiply, [1, 2, 3], 100) == 600


def greeter(person_name, greeting):
    return '{}, {}!'.format(greeting, person_name)


hier = partial(greeter, greeting='Hi')
hellower = partial(greeter, greeting='Hello')

assert hier('Alex') == 'Hi, Alex!'
assert hellower('Misha') == 'Hello, Misha!'

square_list = [number ** 2 for number in range(3)]
assert square_list == [0, 1, 4]

even_list = [number for number in range(3) if number % 2 == 0]
assert even_list == [0, 2]

square_map = {str(number): number ** 2 for number in range(3)}
assert square_map == {'0': 0, '1': 1, '2': 4}

reminders_set = {number % 10 for number in range(3)}
assert reminders_set == {0, 1, 2}

print(f'What type is it? {type(number ** 2 for number in [1,2,3])}')

num_list = range(3)
squared_list = [number ** 2 for number in range(3)]

zipped = zip(num_list, squared_list)
print(f'Zip type is {type(zipped)}')
assert list(zipped) == [(0, 0), (1, 1), (2, 4)]

assert list(zip(filter(bool, range(3)), [x for x in range(3) if x])) == [(1, 1), (2, 2)]
