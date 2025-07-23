import Login as l
import Registration as r
import Main as m


def Projects():
    print()
    options = int(input("1.View 2.Insert 3.back login 4.back Registration 5.main"))
    try:
        if options == 1:
            View()
        elif options == 2:
            Insert()
        elif options == 3:
            l.login()
        elif options == 4:
            r.Registration()
        elif options == 5:
            m.main()
    except ValueError:
        print("you must emter a num")


def Insert():
    while True:
        print(
            """
         1.Title
         2.Details
         3.Total target
         4.Set start/end time
         5.back return
         """
        )
        try:
            choose = int(input("Enter number: "))
            if choose == 1:
                Title = input("Enter Title: ").strip()
                with open("CrowdFundin.txt", "a") as f:
                    f.write(f"Title: {Title}\n")

            elif choose == 2:
                Details = input("Enter Details: ").strip()
                with open("CrowdFundin.txt", "a") as f:
                    f.write(f"Details: {Details}\n")

            elif choose == 3:
                target = input("Enter Total target: ").strip()
                with open("CrowdFundin.txt", "a") as f:
                    f.write(
                        f"target: {target}\n",
                    )
            elif choose == 4:
                time = input("Enter start/end time: ").strip()
                with open("CrowdFundin.txt", "a") as f:
                    f.write(f"time: {time}\n")

            elif choose == 5:
                Projects()

            else:
                print("Erorr\n")
                continue
        except ValueError:
            print("you must emter a num")


def View():
    with open("CrowdFundin.txt") as f:
        print(f.read())
