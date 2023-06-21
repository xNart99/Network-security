import re

print("Your password must contains upper case, lower case,number and symbol")

while True:
    input_password = input("Enter your password: ")

    if len(input_password) < 8 or len(input_password) > 20:
        print("Pass world have to be between 8 to 20 characters.")
        continue
    else:
        if not re.search(r'[A-Z]', input_password):
            print("String should contain at least one uppercase letter")
            continue
        elif not re.search(r'[a-z]', input_password):
            print("String should contain at least one lowercase letter")
            continue
        elif not re.search(r'\d', input_password):
            print("String should contain at least one number letter")
            continue
        elif not re.search(r'\W', input_password):
            print("String should contain at least one symbol letter")
            continue
        else:
            with open("output.txt", "w") as file:
                # Write the text into the file
                file.write(input_password)
                print("File written successfully.")
            break
print("String meets the criteria.")



