n = 1
s = 1
cycles = 500

for i in range(cycles):
    for repeat in range(4):
        n += 2*(i+1)
        s += n

print(s)
