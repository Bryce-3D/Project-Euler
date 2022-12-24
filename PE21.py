from Functions_Module import *

s = 0

for i in range(2,10000):
    l = sumdivisors_proper(i)
    if l != i and sumdivisors_proper(l) == i:
        s += i

print(s)
