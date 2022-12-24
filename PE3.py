def isPrime(n):
    divisors = 0
    for j in range(1,int(i**0.5)):
        if i%j==0:
            divisors = divisors+1
    if divisors==1:
        return True
    else:
        return False


for i in range(1,int(600851475143**0.5)):
    if 600851475143%i==0 and isPrime(i)==True:
        print(i)
        
