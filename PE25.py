a=1
b=1
i=2
digits=1

while digits < 1000:
    a,b,i = b,a+b,i+1
    digits = len( str(b) )

print(i)
print(b)
