def inc(length, start):
    list = []

    for x in range(length):
        list.append(start + x)
    return list


print(inc(10, 4))
