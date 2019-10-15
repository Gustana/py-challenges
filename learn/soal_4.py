limit = int(input("masukkan batas :"))

border = int(limit/2)

def printStar(border) :
    for i in range(border) :
        print("* ", end="")


if limit <= 4 :
    print("bayas harus lebih dari 4")
else :
    printStar(limit)
