def inputnum():

    total = count = 0

    while True:
        num = input("enter num (exit = done) ")

        if num.lower() == "done":
            break

        else:

            number = float(num)
            count += 1
            total += number

    average = total / count
    return total, average, count


total, aver, count = inputnum()

print(f"total {total}")
print(f"count {count}")
print(f"ave {aver}")
