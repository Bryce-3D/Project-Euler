from Functions_Module import *

d=0
n=1
s=1
while d <= 500:
    n += 1
    s = s+n
    d = numdivisors(s)

print(d)
print(s)
print(n)
