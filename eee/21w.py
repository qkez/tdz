from itertools import product
a = product('ИМНОРФ' , repeat = 6 )
k = 1
for i in a:
    b = ''.join(i)
    k += 1
    #print(f"{k} {i}")
    if b == 'ИНФОРМ':
        print(k)
    if k==8000:
        print(b)