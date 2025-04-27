from itertools import product, combinations
q=[]
t=0
a = combinations(iterable=['13','8','5','3','3','2','1','1'] , r = 4 )
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












#print(w)
#u = w[0]
#z = w[1]
#x = w[2]
#c = w[3]
#print(u,   z+x+c, )
#if u <= sum([1:]) and z<= sum([0]+[2:]) and x<= sum([:2]+[3]) and c<=sum([:3]):
#k=1
#print(w)
#e=int(e)
#if [0] <= ([1]+[2]+[3]) and[1]<=([0]+[2]+[3]) and [2]<=([1]+[0]+[3]) and [3]<=([1]+[2]+[0]):
#print(e)