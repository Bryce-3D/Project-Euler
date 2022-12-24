import time
start = time.time()

n = 28433
digits = 10
d = 10**digits

for i in range(7830457):
    n *= 2
    n = n%d

n += 1
print(n)

end = time.time()
print(end-start)
