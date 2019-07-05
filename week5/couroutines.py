
def grep(pattern):
    print('start grep')
    try:
        while True:
            line = yield
            if pattern in line:
                print(line)
    except GeneratorExit:
        print('grep stop')


def grep_python_coroutine():
    g = grep('python')
    yield from g

# g = grep('python')
# next(g)  # g.send(None)
# g.send('golang is better?')
# g.send('python is simple?')


g = grep_python_coroutine()
g.send(None)
g.send('python is wow!')

g.close()


def chain(x_iterable, y_iterable):
    yield from x_iterable
    yield from y_iterable


def the_same_chain(x_iterable, y_iterable):
    for x in x_iterable:
        yield x

    for y in y_iterable:
        yield y


a = [1, 2, 3]
b = (4, 5)

for x in chain(a, b):
    print(x)
