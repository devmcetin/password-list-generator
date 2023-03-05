import os
from passwordGenerator import PasswordGenerator

MIN_LENGTH = 8

currentPath = os.getcwd()
wordlist = open(currentPath + "\\wordlist.txt", "w")

passwordGenerator = PasswordGenerator()
passwordGenerator.generatePassword(4)

for password in PasswordGenerator.passwords:
    if (len(password) >= 8):
        wordlist.write(password + "\n")

wordlist.close()

print(len(PasswordGenerator.passwords), "passwords were entered in the wordlist.txt file.")
