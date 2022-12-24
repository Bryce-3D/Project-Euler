a_1 = [75]
b_1 = [95,64]
c_1 = [17,47,82]
d_1 = [18,35,87,10]
e_1 = [20,4,82,47,65]
f_1 = [19,1,23,75,3,34]
g_1 = [88,2,77,73,7,63,67]
h_1 = [99,65,4,28,6,16,70,92]
i_1 = [41,41,26,56,83,40,80,70,33]
j_1 = [41,48,72,33,47,32,37,16,94,29]
k_1 = [53,71,44,65,25,43,91,52,97,51,14]
l_1 = [70,11,33,28,77,73,17,78,39,68,17,57]
m_1 = [91,71,52,38,17,14,91,43,58,50,27,29,48]
n_1 = [63,66,4,68,89,53,67,30,73,16,69,87,40,31]
o_1 = [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]

b_2 = []
c_2 = []
d_2 = []
e_2 = []
f_2 = []
g_2 = []
h_2 = []
i_2 = []
j_2 = []
k_2 = []
l_2 = []
m_2 = []
n_2 = []
o_2 = []


for i in range(14):
    if o_1[i] >= o_1[i+1]:
        o_2.append(o_1[i])
    else:
        o_2.append(o_1[i+1])

for i in range(13):
    if n_1[i]+o_2[i] >= n_1[i+1]+o_2[i+1]:
        n_2.append(n_1[i]+o_2[i])
    else:
        n_2.append(n_1[i+1]+o_2[i+1])

for i in range(12):
    if m_1[i]+n_2[i] >= m_1[i+1]+n_2[i+1]:
        m_2.append(m_1[i]+n_2[i])
    else:
        m_2.append(m_1[i+1]+n_2[i+1])

for i in range(11):
    if l_1[i]+m_2[i] >= l_1[i+1]+m_2[i+1]:
        l_2.append(l_1[i]+m_2[i])
    else:
        l_2.append(l_1[i+1]+m_2[i+1])

for i in range(10):
    if k_1[i]+l_2[i] >= k_1[i+1]+l_2[i+1]:
        k_2.append(k_1[i]+l_2[i])
    else:
        k_2.append(k_1[i+1]+l_2[i+1])

for i in range(9):
    if j_1[i]+k_2[i] >= j_1[i+1]+k_2[i+1]:
        j_2.append(j_1[i]+k_2[i])
    else:
        j_2.append(j_1[i+1]+k_2[i+1])

for i in range(8):
    if i_1[i]+j_2[i] >= i_1[i+1]+j_2[i+1]:
        i_2.append(i_1[i]+j_2[i])
    else:
        i_2.append(i_1[i+1]+j_2[i+1])

for i in range(7):
    if h_1[i]+i_2[i] >= h_1[i+1]+i_2[i+1]:
        h_2.append(h_1[i]+i_2[i])
    else:
        h_2.append(h_1[i+1]+i_2[i+1])

for i in range(6):
    if g_1[i]+h_2[i] >= g_1[i+1]+h_2[i+1]:
        g_2.append(g_1[i]+h_2[i])
    else:
        g_2.append(g_1[i+1]+h_2[i+1])

for i in range(5):
    if f_1[i]+g_2[i] >= f_1[i+1]+g_2[i+1]:
        f_2.append(f_1[i]+g_2[i])
    else:
        f_2.append(f_1[i+1]+g_2[i+1])

for i in range(4):
    if e_1[i]+f_2[i] >= e_1[i+1]+f_2[i+1]:
        e_2.append(e_1[i]+f_2[i])
    else:
        e_2.append(e_1[i+1]+f_2[i+1])

for i in range(3):
    if d_1[i]+e_2[i] >= d_1[i+1]+e_2[i+1]:
        d_2.append(d_1[i]+e_2[i])
    else:
        d_2.append(d_1[i+1]+e_2[i+1])

for i in range(2):
    if c_1[i]+d_2[i] >= c_1[i+1]+d_2[i+1]:
        c_2.append(c_1[i]+d_2[i])
    else:
        c_2.append(c_1[i+1]+d_2[i+1])

for i in range(1):
    if b_1[i]+c_2[i] >= b_1[i+1]+c_2[i+1]:
        b_2.append(b_1[i]+c_2[i])
    else:
        b_2.append(b_1[i+1]+c_2[i+1])


print(a_1[0]+b_2[0])







    
