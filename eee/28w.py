k=0
for w in range(10,60):
    if str(w) == str(w)[::-1]:
        #print(f"0{w}0")
        k+=1
for q in range(1000,10000):
    if str(q) == str(q)[::-1]:
        #print(q)
        if q % 10000 < 2000  or (q%10==2 and q%100 < 40):
            flag=True
            #print(q)
            if q%100<60:
                #print(q)
                k+=1
                if q==1331:
                    print(f"b){k}")
print(f"a){k}")



