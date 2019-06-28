
def MyRangeGenerator(top):
    current = 0
    while current < top:
        yield current
        current += 1


counter = MyRangeGenerator(10)

for it in counter:
    print(it)
