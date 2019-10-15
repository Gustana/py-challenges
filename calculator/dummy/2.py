#Determine the number wether it's prime or not
def isPrimeNum(num):

    if num%2 == 0 or num%3 == 0 or num%5 == 0:

        if num == 3 or num == 2 or num == 5 :
            return True
        else :
            return False
    else :
        return True

number = 600851475143

i = 2
for i in range(number) :
    if not isPrimeNum(i) :
        continue
    result = number/i
    if result%2 != 0 :
        continue
    print("prime num %d result %d" %(i, result))
    