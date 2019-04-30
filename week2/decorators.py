import functools


def decorator(func):
    print('Decorated func {} inside decorator'.format(func.__name__))
    return func


@decorator
def decorated():
    print('Hello from decorated!')


decorated()


def stringify(func):
    def inner(*args, **kwargs):
        return str(func(*args, **kwargs))
    return inner


@stringify
def multiply(a, b):
    return a * b


multiply_result = multiply(2, 2)

assert multiply_result == '4'


def logger(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('log.txt', 'w') as file:
            file.write(str(result))

        return result
    return wrapped


@logger
def summator(num_list):
    return sum(num_list)


assert summator.__name__ == 'summator'

summator([1, 2, 3, 4])

with open('log.txt', 'r') as file:
    content = file.read()
    assert content == '10'
    print('log.txt content: {}'.format(content))


def advanced_logger(filename):
    def decorator(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'w') as file:
                file.write(str(result))
            return result
        return wrapped
    return decorator


@advanced_logger('new_log.txt')
def advanced_summator(num_list):
    return sum(num_list)

advanced_summator_result = advanced_summator([1, 2, 3, 4, 5])

assert advanced_summator_result == 15

with open('new_log.txt', 'r') as file:
    content = file.read()
    assert content == str(advanced_summator_result)
    print('new_log.txt content: {}'.format(content))


def first_decorator(func):
    def wrapped(*args, **kwargs):
        print('first decorator invocation')
        return func(*args, **kwargs)
    return wrapped


def second_decorator(func):
    def wrapped(*args, **kwargs):
        print('second decorator invocation')
        return func(*args, **kwargs)
    return wrapped


@first_decorator
@second_decorator
def some():
    print('some decorated function')

some()
