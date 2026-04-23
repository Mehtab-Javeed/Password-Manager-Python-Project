from cryptography.fernet import Fernet
import os
print("Welcome to the password manager!")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "passwords.txt")

"""
# This is a function to generate a key and save it into a file
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
"""


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


# master_password = input("Enter your password: ") #master password turned off for now, conflict with fernet
key = load_key()  # + master_password.encode()
fer = Fernet(key)


def view():
    # a means append, w means write r means read, with means it will automatically close the file after we are done
    with open(FILE_PATH, "r") as f:
        for line in f.readlines():
            data = line.rstrip()  # rstrip removes the new line character
            # split the data into user and password
            user, passw = data.split("|")
            # we need to encode the password before we can decrypt it, and then decode it after we decrypt it to get the original password
            print("Account: ", user, " | Password: ",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account Name: ")
    password = input("Password: ")

    # a means append, w means write r means read, with means it will automatically close the file after we are done
    with open(FILE_PATH, "a") as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")


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
