import string
from random import sample

def generatePassword(length, amount):
    all = string.ascii_letters + string.digits + string.punctuation
    with open("passwords.txt", "a") as f:
        for i in range(amount):
            password = "".join(sample(all, length))
            f.write("\n" + password)

generatePassword(9,10)
