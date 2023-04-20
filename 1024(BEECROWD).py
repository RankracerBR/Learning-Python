from math import ceil

n = int(input())

for i in range(n):
    m = str(input())
    m2 = ""
    
    for x in m:
        if(x.isalpha() == True):
            m2 += chr(ord(x) + 3)
        else:
            m2 += x
    
    m3 = m2[::-1]
    s = ceil(len(m3)/2)
    m4 = m3[-s:]
    m5 = ""
    
    for y in m4:
        m5 += chr(ord(y) -1)
    emsg = m3.replace(m4,m5)
    print(emsg)    