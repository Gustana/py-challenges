def isVowel(string) :
    vowelList = []
    for letter in string:
        vowelList.append(letter)
    
    vowelCount = vowelList.count('a') + vowelList.count('i') + vowelList.count('u') + vowelList.count('e') + vowelList.count('o')
    print(vowelCount)
        
string = input("Insert word or sentence :")
isVowel(string)