class Key:

    familyMembers = [
        "mehmet", "cetin"]

    cities = [
        "izmir", "istanbul"]

    teams = [
        "fenerbahce", "galatasaray"]

    symbols = [
        "*", "-", ".", "_"]

    cityCodes = [
        "35", "34"]

    birthYears = [
        "1990", "2000"]

    importantYears = [
        "2023", "1881", "1453"]

    sequences = [
        "1", "123"]

    def __init__(self):
        pass

    def ModifyKey(self, keyList, reverse):

        for i in range(len(keyList)):

            keyList.append(keyList[i].upper())
            keyList.append(keyList[i].title())

            if reverse:
                keyList.append(keyList[i][::-1])
                keyList.append(keyList[i].upper()[::-1])
                keyList.append(keyList[i].title()[::-1])

keyManager = Key()

keyManager.ModifyKey(keyManager.familyMembers, True)
keyManager.ModifyKey(keyManager.cities, False)
keyManager.ModifyKey(keyManager.teams, False)

sumOfKeys = sum([keyManager.familyMembers, keyManager.cities, keyManager.teams,
                 keyManager.symbols, keyManager.cityCodes, keyManager.birthYears,
                 keyManager.importantYears, keyManager.sequences], [])