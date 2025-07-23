import Registration as r
import Projects as p
import Login as l


def Menu():
    print("Menu")
    print("1.registration")
    print("2.Login")
    print("3.exit")


def main():
    while True:
        print()
        Menu()
        try:
            choose = int(input("Enter number: "))
            if choose == 1:
                r.Registration()
            elif choose == 2:
                l.login()
            elif choose == 3:
                break
            else:
                print("Erorr")
        except ValueError:
            print("you must emter a num")


if __name__ == "__main__":
    main()
