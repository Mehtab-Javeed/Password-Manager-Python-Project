master_password = input("Enter your password: ")


def view():
    # a means append, w means write r means read, with means it will automatically close the file after we are done
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()  # rstrip removes the new line character
            # split the data into user and password
            user, password = data.split("|")
            print("Account: " + user + " | Password: " + password)


def add():
    name = input("Account Name: ")
    password = input("Password: ")

    # a means append, w means write r means read, with means it will automatically close the file after we are done
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + password + "\n")  # \n means new line


while True:
    mode = input(
        "Would you like to add new password or view existing ones (add, view), press Q to quit? ").lower()
    if mode == "q":
        print("Exiting password manager.")
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
