from itertools import product, permutations
a=permutations(iterable="QWERTYUIOPASDFGHJKLZXCVBNM",r=3)
b=product("123456789", repeat=3)
k=0
for i in a:
    c = ''.join(i)
    #print(c)
    k+=1
    for j in b:
        f = ''.join(j)
        f=int(f)
        if f % 11==0 and 100 <= f <= 999:
            #print(f"{c}{f}")
            k += 1
print(k)