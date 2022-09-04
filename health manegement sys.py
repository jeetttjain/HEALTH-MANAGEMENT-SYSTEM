def gettime():
    import datetime
    return datetime.datetime.now()


def log():
    print("choose your client")
    client = int(input("1.Jeet\n2.Jay\n3.Rishabh\n"))
    if client == 1:
        print(" what do you want to log for jeet")
        choice = int(input("1.diet\n2.exercise\n"))
        if choice == 1:
            f = open("jeet diet.txt", "a")
            data = input("Enter what has Jeet eaten?\n")
            f.write(str([str(gettime())]) + " " + data + "\n")
            f.close()
        else:
            f = open("jeet exercise.txt", "a")
            data = input("how much time has Jeet worked out?\n")
            f.write(str([str(gettime())]) + " " + data + "\n")
            f.close()
        # con = int(input("Do you want to log more for Harry? \n1. Yes \n2. No"))
    elif client == 2:
        print(" what do you want to log for jeet")
        choice = int(input("1.diet\n2.exercise\n"))
        if choice == 1:
            f = open("jay diet.txt", "a")
            data = input("Enter what has Jay eaten?\n")
            f.write(str([str(gettime())]) + " " + data + "\n")
            f.close()
        else:
            f = open("jay exercise.txt", "a")
            data = input("how much time has Jay worked out?\n")
            f.write(str([str(gettime())]) + " " + data + "\n")
            f.close()
        # con = int(input("Do you want to log more for Harry? \n1. Yes \n2. No"))
    elif client == 3:
        print(" what do you want to log for Rishabh")
        choice = int(input("1.diet\n2.exercise\n"))
        if choice == 1:
            f = open("rishabh diet.txt", "a")
            data = input("Enter what has Rishabh eaten?\n")
            f.write(str([str(gettime())]) + " " + data + "\n")
            f.close()
        else:
            f = open("rishabh exercise.txt", "a")
            data = input("how much time has Rishabh worked out?\n")
            f.write(str([str(gettime())]) + " " + data + "\n")
            f.close()
        # con = int(input("Do you want to log more for Harry? \n1. Yes \n2. No"))
    else:
        print("Enter proper client Id...")


def retrieve():
    print("choose your client")
    client = int(input("1.Jeet\n2.Jay\n3.Rishabh\n"))
    if client == 1:
        print("what do you want to retrieve for jeet?")
        choice = int(input("1.diet\n2.exercise\n"))
        if choice == 1:
            f = open("jeet diet.txt", "r")
            print(f.readlines())
            f.close()
        elif choice == 2:
            f = open("jeet exercise.txt", "r")
            print(f.readlines())
            f.close()

    elif client == 2:
        print("what do you want to retrieve for jay?")
        choice = int(input("1.diet\n2.exercise\n"))
        if choice == 1:
            f = open("jay diet.txt diet.txt", "r")
            print(f.readlines())
            f.close()

        elif choice == 2:
            f = open("jay exercise.txt", "r")
            print(f.readlines())
            f.close()

    elif client == 3:
        print("what do you want to retrieve for Rishabh?")
        choice = int(input("1.diet\n2.exercise"))
        if choice == 1:
            f = open("rishabh diet.txt", "r")
            print(f.readlines())
            f.close()

        elif choice == 2:
            f = open("rishabh exercise.txt", "r")
            print(f.readlines())
            f.close()


print("WELCOME TO HEALTH MANAGEMENT")
ch = int(input("1.diet\n2.Activity"))
if ch == 1:
    log()
elif ch == 2:
    retrieve()
else:
    print("Please Enter correct choice")
