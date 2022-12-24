from Functions_Module import *

i=2
no=1

while no <= 10000:
    i += 1
    if isprime(i) == True:
        no += 1

print(i)
