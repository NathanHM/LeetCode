ransomNote = "a"
magazine = "b"

def validRansom (ransomNote, magazine):

    dict = {}

    for c in range(len(magazine)):
        if magazine[c] not in dict:
            dict[magazine[c]] = [True]
        else:
            dict[magazine[c]].append(True)

    for c in range(len(ransomNote)):
        if ransomNote[c] not in dict:
            return False
        else:
            if True not in dict[ransomNote[c]]:
                return False
            else:
                dict[ransomNote[c]].remove(True)

    return True


print(validRansom(ransomNote, magazine))