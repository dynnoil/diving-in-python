import sys

digit_string = sys.argv[1]
string_length = len(digit_string)

result = 0

for i in range(string_length):
    result += int(digit_string[i])

print(result)
