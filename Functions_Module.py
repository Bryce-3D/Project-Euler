def gcd(a,b):
    while a != b:
        while b > a:
            b = b-a
        while a > b:
            a = a-b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

def fac(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else: 
        k=1
        for i in range(1,n+1):
            k = k*i
        return k

def choose(a,b):
    if b >= 0 and a >= b:
        ans = 1
        b = min(b,a-b)
        for i in range(1,b+1):
            ans = ans*(a+1-i)//i
        return ans
    else:
        return 0
        
def perm(a,b):
    ans = 1
    for i in range(1,b+1):
        ans *= (a+1-i)
    return ans

def isqrt(n):
    k = int(n**0.5)
    if k**2 <= n:
        while k**2 <= n:
            k += 1
        return k-1
    else:
        while k**2 > n:
            k -= 1
        return k

def isprime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        k = isqrt(n)
        for i in range (2,k+1):
            if n%i == 0:
                return False
        return True

def iscomposite(n):
    if n == 1:
        return False
    elif isprime(n) == True:
        return False
    else:
        return True
        

def ispalindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False

def numdivisors(n):
    d = 0
    sqrt = isqrt(n)
    for i in range(1,sqrt):
        if n%i == 0:
            d +=2
    if n%sqrt == 0:
        if sqrt**2 == n:
            d += 1
        else:
            d += 2
    return d

def sumdivisors(n):
    s = 0
    sqrt = isqrt(n)
    for i in range(1,sqrt):
        if n%i == 0:
            s += i + n//i
    if n%sqrt == 0:
        if sqrt**2 == n:
            s += sqrt
        else:
            s += sqrt + n//sqrt
    return s

def sumdivisors_proper(n):
    return sumdivisors(n)-n

def sumdigits(n):
    m = str(n)
    l = len(m)
    s = 0
    for i in range(l):
        s += int(m[i])
    return s

def sumdigits_squared(n):
    m = str(n)
    l = len(m)
    s = 0
    for i in range(l):
        s += int(m[i])**2
    return s






