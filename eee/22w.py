from itertools import product
k=0
q=[]
y=[]
m=[]
t='1'
v=0
a = product('10' , repeat = 6 )
for i in a:
    q.append(i)
    w=''.join(i)
    if w.startswith(t):
        y.append(w)
for u in y:
    o=''.join(y)
    if u.count('1')==2 or u.count('1')==4 or u.count('1')==6:
        m.append(u)
        v+=1
        #print(u)
for u in y:
    o=''.join(y)
    if u.count('1')==1 or u.count('1')==3 or u.count('1')==5:
        m.append(u)
        v+=1
        #print(u)
for g in m:
    g = int(g)
    if g % 8 == 0:
        k += 1
        #print(g)
print(k)