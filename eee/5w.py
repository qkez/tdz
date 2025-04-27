from itertools import product
k=0
w={-1,-2,+1,+2}
r=[]
q=product(w,repeat=4)
for e in q:
    #print(e)
    r.append(e)
   # print(e)
    #print(type(e))
    t=0
    for y, item in enumerate(e):
        t+=item
    #print(t)
    if t==5:
        k+=1
print(k)

