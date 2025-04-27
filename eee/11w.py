from itertools import product
a = product('АГИЛМОРТ' , repeat = 8 )
k = 1
for i in a:
    b = ''.join(i)
    k += 1
    #print(f"{k} {i}")
    if b == 'АЛГОРИТМ':
        print(k)
    if k == 202402:
        print(b)