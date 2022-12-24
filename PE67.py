L = []
with open('PE67_Triangle.txt') as f:
    for line in f.readlines():
        L.append(list(map(int,line[:-1].split())))

x = []
for i in range(100):
    x.append(0)
L.append(x)

def optimized_sum_row(m,n):
    if len(m) != len(n):
        print('hey recheck your work bro')
        return
    else:
        l = []
        for i in range(len(m)-1):
            if m[i]+n[i] >= m[i+1]+n[i+1]:
                l.append(m[i]+n[i])
            else:
                l.append(m[i+1]+n[i+1])
        return(l)

for i in range(99,0,-1):
    L[i] = optimized_sum_row(L[i],L[i+1])

print(L[0][0]+L[1][0])
