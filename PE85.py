import time
start = time.time()

from Functions_Module import *

def C2(n):
    return choose(n,2)

given = 2000000
cap = 1

while C2(cap) <= isqrt(given):
    cap += 1

t = given
r = [0,0]

for m in range(1,cap):
    n = m
    while C2(m+1)*C2(n+1) <= given:
        n += 1
    if abs( given-C2(m+1)*C2(n) ) < t:
        t = abs( given-C2(m+1)*C2(n) )
        r = [m,n-1]
    if abs( given-C2(m+1)*C2(n+1) ) < t:
        t = abs( given-C2(m+1)*C2(n+1) )
        r = [m,n]

print(t)
print(r)
print( int(r[0])*int(r[1]) )

end = time.time()
print(end-start,"seconds")
        
    
