import random
import hashlib

salt = int(random.uniform(1, 100000))
salt_bytes = str(salt).encode('utf-8')
input_password = input("Enter your password: ")
data = input_password.encode('utf-8') + salt_bytes
hash_object = hashlib.sha256()
hash_object.update(data)
hashed_value = hash_object.hexdigest()
print(f"Salt: {salt}")
print(f"Hashed value: {hashed_value}")



