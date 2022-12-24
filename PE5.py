def gcd(a,b):
    while a != b:
        while b > a:
            b = b-a
        while a > b:
            a = a-b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

n=1
for i in range (1,21):
    n = lcm(i,n)

print(n)
