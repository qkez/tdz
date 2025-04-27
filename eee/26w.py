from itertools import product, combinations
q=[]
t=0
a = combinations(iterable=['11','10','9','8','7','6','5','4','3'] , r = 3 )
for i in a:
    q.append(i)
    #print(type(q))
    e = ' '.join(i)
    #print(e)
    r=(sum(map(int,e.split( ))))
    #print(r)
    a=e[0]
    a=int(a)
#   print(a)
    if a**2 == ((r-a)**2 -2*r):
       # print(e)
        t+=1
print(t)