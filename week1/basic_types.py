# Int
num = 18
num = 0
num = -9
num = 100_000_000
num_type = type(num)
print(num_type)

# Float
float_num = 18.1
float_num = 0.0
float_num = -9.5
print(type(float_num))

# Convertation
num = 100.5
num = int(num)
print(num)
assert num == 100
num = float(num)
print(num)
assert num == 100.0

# Strings
example_str = "String"
print(example_str)
print(type(example_str))

city = "Москва"
assert city[::-1] == "авксоМ"

# String formatting
template = "%s - главное достоинство программиста. (%s)"
print(template % ("Лень", "Larry Wall"))

another_template = "{} - главное достоинство программиста. ({})"
print(another_template.format("Лень", "Larry Wall"))

another_one_template = "{what} - главное достоинство программиста. ({author})"
print(another_one_template.format(what="Лень", author="Larry Wall"))

what = "Лень"
author = "Larry Wall"
f_string_template = f"{what} - главное достоинство программиста. ({author})"
print(f_string_template)

example_bytes = b"hello"
print(type(example_bytes))

for byte in example_bytes:
    print(byte)

