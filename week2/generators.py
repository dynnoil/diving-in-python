
def even_range(start, end):
    current = start
    while current < end:
        yield current
        current += 2


for number in even_range(0, 10):
    print(number)

ranger = even_range(0, 4)

assert next(ranger) == 0

assert next(ranger) == 2

try:
    next(ranger)
except StopIteration as error:
    print(error)


def list_generator(list_obj):
    for item in list_obj:
        yield item
        print('After yielding {}'.format(item))


generator = list_generator([1, 2])

assert next(generator) == 1
assert next(generator) == 2


def fibonacci(number):
    a = b = 1
    for _ in range(number):
        yield a
        a, b = b, a + b


print('\nFibonacci: ')
for num in fibonacci(10):
    print(num)


def accumulator():
    total = 0
    while True:
        value = yield total
        print('Got: {}'.format(value))
        if not value:
            break
        total += value


acc = accumulator()

next(acc)

print('Accumulated: {}'.format(acc.send(1)))
print('Accumulated: {}'.format(acc.send(2)))
print('Accumulated: {}'.format(acc.send(5)))
