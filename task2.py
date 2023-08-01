

import string
import random


def generate_password(length):

    character = string.ascii_letters + string.digits + string.punctuation


    password = ''.join(random.choice(character) for i in range(length))

    return password


length = int(input("Enter the Length of the desired password "))
password = generate_password(length)

print("Your randomly generated password is: ", password)
