import itertools
from key import sumOfKeys

class PasswordGenerator:

    passwords = list()

    def __init__(self):
        pass

    def generatePassword(self, maxCombine):

        print("Password combinations are being generated.")
        print("This process may take several minutes, depending on the number of keywords.")

        for i in range(maxCombine):
            keys = list()

            for j in range(i + 1):
                keys.append(sumOfKeys)

            combines = list(itertools.product(*keys))

            for combine in combines:
                password = ""

                for key in combine:
                    password += key

                self.passwords.append(password)
