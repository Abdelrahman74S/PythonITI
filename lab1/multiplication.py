list1 = []

n = int(input("enter num: "))

for i in range(1, n + 1):
    list2 = []
    for j in range(1, i + 1):
        list2.append(j * i)
    list1.append(list2)
print(list1)
