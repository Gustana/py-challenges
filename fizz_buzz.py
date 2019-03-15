numStart = int(input("Insert number range from :"))
numEnd = int(input("Insert number range to :"))

while numEnd >= numStart :
    if numStart%3 == 0 :
        print("fizz")
    elif numStart%5 == 0 :
        print("buzz")
    else :
        print(numStart)
    numStart+=1