import random
import string
chars = string.ascii_letters + string.digits + string.punctuation
# print(random.choice(chars))

length = int(input('Password Length: '))
password = ""

for _ in range(length):
    c = random.choice(chars)
    password += c

print(f'Your password is; {password}')