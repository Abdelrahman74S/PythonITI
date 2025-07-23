def AskNmae():

    while True:
        name = input("enter name: ")
        if name == "" or name.isdigit():
            print("Enter a again:")
        else:
            break
    while True:
        email = input("enter email: ")
        if "@" in email and "." in email:
            print("email is OK")
            break
        else:
            print("enter agin")

    print(f"name:{name}")
    print(f"email:{email}")


AskNmae()
