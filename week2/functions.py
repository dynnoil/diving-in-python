from datetime import datetime


def get_seconds():
    """Return current seconds"""
    return datetime.now().second


print(f"{get_seconds.__doc__}: {get_seconds()}")


def get_none():
    pass


assert get_none() == None


def add(x: int, y: int) -> int:
    return x + y


assert add(1, 2) == 3
assert add('still ', 'works') == 'still works'


def extender(source_list: list, extend_list: list):
    source_list.extend(extend_list)


values = [1, 2, 3]
extender(values, [4, 5, 6])
assert values == [1, 2, 3, 4, 5, 6]


def replacer(source_tuple: tuple, replace_with: tuple):
    source_tuple = replace_with


user_info = ('Guido', '31/01')
replacer(user_info, ('Larry', '30/03'))

assert user_info == ('Guido', '31/01')


def say(greeting, name):
    print(f"{greeting} {name}!")


print(say(name="Kitty", greeting="Hello"))

result = 0


def increment():
    result += 1
    return result


try:
    increment()
except UnboundLocalError as error:
    print(error)


def append_one(iterable=[]):
    iterable.append(1)
    return iterable


assert append_one() == [1]
assert append_one() == [1, 1]


def function(iterable=None):
    if iterable is None:
        iterable = []


def another_function(iterable=None):
    iterable = iterable or []


def printer_args(*args):
    print(type(args))

    for argument in args:
        print(argument)


printer_args()

printer_args(1, 2, 3, 4, 5)

name_list = ['John', 'Bull']

printer_args(*name_list)


def printer_kwargs(**kwargs):
    print(type(kwargs))

    for key, value in kwargs.items():
        print(f"{key}: {value}")


printer_kwargs()

printer_kwargs(name="Vlad", age=12)

person = {
    'name': 'Petr',
    'age': 20
}

printer_kwargs(**person)

