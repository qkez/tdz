from itertools import product, permutations
a=permutations(iterable="QWERTYUIOPASDFGHJKLZXCVBNM",r=4)
b=product("1234567890", repeat=2)
k=0
for i in a:
    c = ''.join(i)
    k+=1
    for j in b:
        f = ''.join(j)
        f=int(f)
        if f%7==0 and 10 <= f <= 99:
            k+=1
            #print(f"{c}{f}")
print(k)




