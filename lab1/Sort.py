n = int (input("enter 5 elements: "))

list =[]
if n == 5:
    for i  in range(n):
      num = int(input("enter elements: "))
      list.append(num)
    print(list)
    list.sort()
    print("ascending")
    print(list)
    list.reverse()
    print("descending")
    print(list)
else:
    print("only 5 elements")


# list = []
#
# while True:
#  elements = input("enter elements: ").split()
#
#  if len(elements) == 5:
#     for i  in range(len(elements)):
#       list= elements
#     print(list)
#     list.sort()
#     print("ascending")
#     print(list)
#     list.reverse()
#     print("descending")
#     print(list)
#     break
#  else:
#     print("only 5 elements")
