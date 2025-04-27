from itertools import permutations
from os import remove
e=[]
k=0
a=permutations(iterable="РЕСУРС",r=6)
for i in a:
    b= ''.join(i)
    r=b.count("СС")
    t = b.count("РР")
    if r==0 and t==0:
        k+=1
        #print(b)
print(k)




