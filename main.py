import random
import string

length = random.randint(8, 20)

characters = string.ascii_letters + string.digits + string.punctuation

random_string = ''.join(random.choice(characters) for i in range(length))

print("Generated string:", random_string)
