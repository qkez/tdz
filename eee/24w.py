from itertools import permutations
from os import remove
e=[]
k=0
a=permutations(iterable="AABBCC",r=6)
for i in a:
    b= ''.join(i)
    e.append(b)
for h in e:
    r = h.count("AA")
    t = h.count("BB")
    v = h.count("CC")
    if r==0 and t==0 and v==0:
        k+=1
        #print(h)
print(k)
