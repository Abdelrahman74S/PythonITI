import re

Email = ""
password = ""


def Registration():
    global Email, password
    print("Registration:")
    namefrist = input("Enter First name: ")
    namelast = input("Enter Last name: ")

    Email = input("Enter Email: ")
    regexEmail = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"

    if re.fullmatch(regexEmail, Email):
        print("Valid Email")

    else:
        print("Invalid Email")
        return

    password = input("Enter password: ")
    Confirmpassword = input("Enter Confirm password: ")

    if password == Confirmpassword:
        print("Valid password")
    else:
        print("Invalid password")
        return
    Mobile = input("Enter Mobile: ")
    regexMobile = r"^(\+201|01|00201)[0-2,5]{1}[0-9]{8}"

    if re.fullmatch(regexMobile, Mobile):
        print("Valid Mobile")

    else:
        print("Invalid Mobile")
        return
    try:
        with open("users.txt", "a") as f:
            f.write(
                f"frist name: {namefrist},last name: {namelast},Email: {Email},password: {password},Mobile: {Mobile}\n"
            )
        print("Registration completed and saved!")
    except Exception as e:
        print("Error saving user:", e)
