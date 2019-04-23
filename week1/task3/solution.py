import sys

steps_number = int(sys.argv[1])

for step in range(1, steps_number + 1):
    spaces = steps_number - step
    print(' ' * spaces + '#' * step)
