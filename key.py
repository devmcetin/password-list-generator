class Key:

    familyMembers = list()
    cities = list()
    teams = list()
    symbols = list()
    cityCodes = list()
    birthYears = list()
    importantYears = list()
    sequences =  list()

    def __init__(self):
        pass

    def modifyKey(self, keyList, reverse):

        for i in range(len(keyList)):

            keyList.append(keyList[i].upper())
            keyList.append(keyList[i].title())

            if reverse:
                keyList.append(keyList[i][::-1])
                keyList.append(keyList[i].upper()[::-1])
                keyList.append(keyList[i].title()[::-1])

    def getKeys(self, keyList, nameOfList):
        keyList.clear()

        print("\n<<< {} KEYS >>>".format(nameOfList))

        while True:
            key = input("Enter a key (For quit : \"Q\") :   ")

            if (key.upper() == "Q"):
                break
            else:
                keyList.append(key.strip())

keyManager = Key()

keyManager.getKeys(keyManager.familyMembers, "Members of Family")
keyManager.getKeys(keyManager.cities, "Associated Cities")
keyManager.getKeys(keyManager.teams, "Teams")
keyManager.getKeys(keyManager.symbols, "Special Symbols")
keyManager.getKeys(keyManager.cityCodes, "City Codes")
keyManager.getKeys(keyManager.birthYears, "Birthyears")
keyManager.getKeys(keyManager.importantYears, "Important Years")
keyManager.getKeys(keyManager.sequences, "Sequences")

keyManager.modifyKey(keyManager.familyMembers, True)
keyManager.modifyKey(keyManager.cities, False)
keyManager.modifyKey(keyManager.teams, False)

sumOfKeys = sum([keyManager.familyMembers, keyManager.cities, keyManager.teams, keyManager.symbols,
                keyManager.cityCodes, keyManager.birthYears, keyManager.importantYears, keyManager.sequences], [])
