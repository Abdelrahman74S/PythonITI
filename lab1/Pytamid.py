n = int(input("enter num: "))

for x in range(1, n + 1):
    for y in range(x + 1):
        space = n - y
    print(" " * space + "*" * y)
