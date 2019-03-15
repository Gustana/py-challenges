#Determine the number wether it's prime or not
def isPrimeNum(num):

    if num%2 == 0 or num%3 == 0 or num%5 == 0:

        if num == 3 or num == 2 or num == 5 :
            return True
        else :
            return False
    else :
        return True

#Find the next prime number
def nextPrimary(num):

    primeNum = num

    if isPrimeNum(primeNum):
        if primeNum == 2 :
            primeNum+=1
            print("Next prime number is %d" %primeNum)
        else :
            primeNum+=2
            while not isPrimeNum(primeNum) :
                primeNum+=2
            print("Next prime number is %d" %primeNum)
    else :        
        print("Not prime number")


#ask number
def askNum():
    num = int(input("Input Prime Number : "))
    nextPrimary(num)

askNum()