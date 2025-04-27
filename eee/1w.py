from itertools import product
a = product('АКМОСТ' , repeat = 6 )
k = 1
for i in a:
    b = ''.join(i)
    k += 1
    #print(f"{k} {i}")
    if b == 'КОСМОС':
        print(k)
