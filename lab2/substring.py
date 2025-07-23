def substring(str):
    str = str.lower()

    string1 = current = str[0]

    start = 0

    for i in range(1, len(str)):
        if str[i] >= str[i - 1]:
            current += str[i]
        else:
            if len(current) > len(string1):
                string1 = current
                current = str[i]

    if len(string1) > len(current):
        string1 = current
    print(f"longest is {string1}")


str = "Abdulrahman"
str1 = "Abdelrahman"
substring(str)
substring(str1)
