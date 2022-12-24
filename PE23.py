from Functions_Module import *

L_abundant = []
for i in range(1,28124):
    if sumdivisors_proper(i) > i:
        L_abundant.append(i)

l = len(L_abundant)
L_pairsum = set()
for i in range(l):
    for j in range(i,l):
        a = L_abundant[i]+L_abundant[j]
        if a < 28124:
            L_pairsum.add(a)
        else:
            break

s = 0
for i in range(1,28124):
    if i not in L_pairsum:
        s += i

print(s)
        
    
    
