best_girl=0
longest=0

for i in range (1,1000000):
    l=1
    j=i
    while i != 1:
        if i%2 == 0:
            i = i/2
            l += 1
        else:
            i = 3*i+1
            l += 1
    if l > longest:
        best_girl = j
        longest = l

print(best_girl)
