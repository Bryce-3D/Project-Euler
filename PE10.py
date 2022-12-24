from Functions_Module import *

s=0

for i in range(1,2000000):
    if isprime(i) == True:
        s = s+i

print(s)
