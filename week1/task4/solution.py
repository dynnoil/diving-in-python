import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])


def evaluate(a, b, discriminant):
    return (-b + discriminant) / 2 * a


discriminant = math.sqrt(b ** 2 - 4 * a * c)

x1 = int(evaluate(a, b, -discriminant))
x2 = int(evaluate(a, b, discriminant))

result = f"{x1}\n{x2}"

print(result)
