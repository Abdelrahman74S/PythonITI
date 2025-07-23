def divisible(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"

    elif number % 5 == 0:
        return "buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return "Erorr"


print(divisible(9))
print(divisible(15))
print(divisible(30))
print(divisible(20))
print(divisible(45))
