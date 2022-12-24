from Functions_Module import *

k = 1
works = True

while works == True:
    k += 2
    if iscomposite(k) == True:
        m = (k-1)//2
        for i in range(1,isqrt(m)+1):
            d = k - 2*i**2
            if isprime(d) == True:
                works = True
                break
            works = False

print(k)
