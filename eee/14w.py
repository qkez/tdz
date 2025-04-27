from itertools import permutations
k=0
a=permutations(iterable="БАНАНА",r=6)
for i in a:
    #print(i)
    #k+=1
    b = ''.join(i)
    r = b.count("НН")
    if r >0 :
        k += 1
        #print(b)

print(k)