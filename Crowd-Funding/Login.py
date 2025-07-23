import Registration as r
import Projects as p


def login():
    Email = input("Enter Email: ")
    password = input("Enter password: ")

    if Email == r.Email and password == r.password:
        print("correct")
        p.Projects()
    else:
        print("password or Email not correct")
