import os

filename = os.getcwd() + '/week2/sets.py'

file = open(filename, 'r')

print(file.read())

file.close()

with open(filename) as f:
    print(f.read())
