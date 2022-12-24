import time
start = time.time()

from Functions_Module import *

L_1 = [1]
L_89 = [89]
t = 1

for i in [x for x in range(1,568) if x != 89]:
    store = i
    while i not in L_1 and i not in L_89:
        i = sumdigits_squared(i)
    if i in L_1:
        L_1.append(store)
    else:
        L_89.append(store)
        t += 1


for i in range(568,10000000):
    if sumdigits_squared(i) in L_89:
        t += 1

print(t)

end = time.time()
print(end - start)
