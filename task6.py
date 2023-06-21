import re
import random
import hashlib


def init_password():
    print("Your password must contain an uppercase letter, a lowercase letter, a number, and a symbol.")
    while True:
        input_password = input("Enter your password: ")
        if len(input_password) < 8 or len(input_password) > 20:
            print("Password must be between 8 and 20 characters.")
            continue
        else:
            if not re.search(r'[A-Z]', input_password):
                print("Password must contain at least one uppercase letter.")
                continue
            elif not re.search(r'[a-z]', input_password):
                print("Password must contain at least one lowercase letter.")
                continue
            elif not re.search(r'\d', input_password):
                print("Password must contain at least one number.")
                continue
            elif not re.search(r'\W', input_password):
                print("Password must contain at least one symbol.")
                continue
            else:
                save_password(hash_password(input_password))
                main()
                break


def save_password(string):
    with open("output.txt", "w") as file:
        # Write the text into the file
        file.write(string)


def hash_password(password):
    data = password.encode('utf-8')
    hash_object = hashlib.sha256()
    hash_object.update(data)
    hashed_value = hash_object.hexdigest()

    return hashed_value


def check_file():
    try:
        with open("output.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return False


def verify_password(string):
    hashed_password = hash_password(string)

    read_password = check_file()
    if read_password and hashed_password == read_password:
        print("Password verification successful.")
    else:
        print("Password verification failed.")


def main():
    menu = "Menu:\n1. Create Password\n2. Verify Password"
    print(menu)
    input_choice = input("Enter your choice: ")

    if input_choice == "1":
        init_password()
    elif input_choice == "2":
        input_password = input("Please input your password for verification: ")
        verify_password(input_password)
    else:
        print("Invalid choice.")


main()
