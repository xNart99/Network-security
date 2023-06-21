import hashlib


def hash_string(string):
    hash_object = hashlib.sha256()
    hash_object.update(string.encode('utf-8'))
    hashed_string = hash_object.hexdigest()
    return hashed_string


input_password = input("Enter your password: ")

hashed_password = hash_string(input_password)

verify_password = input("Enter your password for verification: ")

hashed_verify = hash_string(verify_password)

if hashed_password == hashed_verify:
    print("Password verification successful.")
else:
    print("Password verification failed.")