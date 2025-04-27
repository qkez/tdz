from itertools import product
k=0
q=[]
y=[]
t='1'
a = product('210' , repeat = 5 )
for i in a:
    q.append(i)
    w=''.join(i)
    if w.startswith(t):
        y.append(w)
for u in y:
    o=''.join(y)
    u=int(u)
    if u%3==0:
        k+=1
        #print(u)
print(k)