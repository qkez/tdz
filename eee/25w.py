from itertools import product
k=0
t=0
s=0
p=0
w={0,+1}
r=[]
o=[]
q=product(w,repeat=5)
u=product(w,repeat=5)
for e in q:
    #print(e)
    r.append(e)
    t = sum(e)
    #print(t)
    if t==3:
        k+=1
for i in u:
    #print(i)
    o.append(i)
    p = sum(i)
    #print(p)
    if p==2:
        s+=1

print(s*k)
#print(k)
#print(s)




