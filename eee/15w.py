from itertools import product
k=0
t=0
l=0
w={-1,-3,+1,+3}
r=[]
q=product(w,repeat=6)
for e in q:
    #l+=1
    r.append(e)
    #print(e)
    t=sum(e)
    #print(t)
    if t==4:
        k+=1
print(k)
#print(l)