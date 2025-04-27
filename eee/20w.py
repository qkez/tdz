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
        g = e.count("5")
        if g ==3 :
            o += 1
            #print(e)
        if k==28345:
            print(f"b){e}")

#print(n)
print(f"a){o}")
