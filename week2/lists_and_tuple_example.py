from random import randint
import statistics

numbers = []
numbers_size = randint(15, 20)

for _ in range(numbers_size):
    numbers.append(randint(10, 20))

print(numbers)

# mutates list
numbers.sort()

half_size = len(numbers) // 2
median = None

if numbers_size % 2 == 1:
    median = numbers[half_size]
else:
    median = sum(numbers[half_size - 1:half_size + 1]) / 2

print(f"Median: {median}")

assert median == statistics.median(numbers)
