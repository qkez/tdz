from itertools import product
r=0
t=0
k=0
o=0
y=[]
q=product("0123456789",repeat=6)
for w in q:
    e = ' '.join(w)
    y.append(e)
    r=e[:5]
    t=e[5:]
    z=(sum(map(int,r.split( ))))
    x=(sum(map(int,t.split( ))))
    if z==x:
        k += 1
        g = e.count("6")
        if g ==2 :
            o += 1
        m=1135246//k
        n=1135246-(m*k)
        if k==30206:
            print(f"b){e}")

#print(n)
print(f"a){o}")


