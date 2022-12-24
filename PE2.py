a=1
b=2
s=2

while b <= 4000000:
    a,b = b,a+b
    if b%2==0:
        s = b+s

print(s)
