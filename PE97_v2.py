import time
start = time.time()

n = 28433
digits = 10
d = 10**digits

for i in range(783045):
    n *= 2**10
    n = n%d

n *= 2**7
n = n%d

n += 1
print(n)

end = time.time()
print(end-start)
