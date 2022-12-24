import time
start = time.time()

pan = {1,2,3,4,5,6,7,8,9}

a = 1
b = 1
i = 2
pandigital = False

while pandigital == False:
    a,b,i = b,a+b,i+1
    bstr = str(b)
    try:
        front = set()
        back = set()
        for i in range(9):
            front.add(bstr[i])
            back.add(bstr[-i-1])
        if front == pan and back == pan:
            pandigital = True
    except:
        pass

print(i)

end = time.time()
print(end - start)

#as of now this would kill the laptop DO NOT RUN
            
