
empty_set = set()

number_set = {1, 2, 3, 4, 5, 5}

print(number_set)

assert 2 in number_set

odd_set = set()
even_set = set()

for number in range(10):
    if number % 2:
        odd_set.add(number)
    else:
        even_set.add(number)

print(f"Odd set: {odd_set}")
print(f"Even set: {even_set}")

assert odd_set | even_set == odd_set.union(even_set)
assert odd_set & even_set == odd_set.intersection(even_set)

frozen = frozenset(['a', 'b', 'c'])

try:
    frozen.add('d')
except AttributeError as error:
    print(error)
finally:
    print('Its Ok, go futher')
