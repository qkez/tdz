from itertools import product, combinations
q=[]
t=0
a = combinations(iterable=['55','34','21','13','8','5','3','2','1'] , r = 5 )
for i in a:
    q.append(i)
    #print(type(q))
    e = '  '.join(i)
    #print(e)
    r=(sum(map(int,e.split( ))))
    #print(r)
    a=e[0]
    a=int(a)
#   print(a)
    if a < (r - a):
       # print(e)
        t+=1
print(t)