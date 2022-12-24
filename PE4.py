from Functions_Module import *

ans = 0
for a in range(100,1000):
    for b in range(100,1000):
        if ispalindrome(a*b) == True and a*b > ans:
            ans = a*b

print(ans)
        
