def countFactorial(num) :
    angka = num
    result = 1
    while (angka>1) :
        result *=angka
        angka-=1
    return result

n = int(input("masukkan n :"))
r = int(input("masukkan r :"))

factorial_n = countFactorial(n)
factorial_r = countFactorial(r)

diff = n-r

factorial_n_r = countFactorial(diff)

hasil = factorial_n/(factorial_r*factorial_n_r)

print(factorial_n)
print(factorial_r)
print(factorial_n_r)

print(hasil)