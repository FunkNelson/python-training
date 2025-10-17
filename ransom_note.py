def canConstruct(ransomNote: str, magazine: str) -> bool:

    constructable = True

    magazine_dic = {}

    for letter in magazine:
        if letter in magazine_dic:
            magazine_dic[letter] += 1
        else:
            magazine_dic[letter] = 1

    for letter in ransomNote:
        if letter in magazine_dic and magazine_dic[letter] > 0:
            magazine_dic[letter] -= 1
        else:
            constructable = False
            break

    return constructable


print(canConstruct("moop", "nmnmnmmmooooooooopppppp"))
print(canConstruct("jjjj", "jj"))
