k=0
for q in range(100000,1000000):
    if str(q) == str(q)[::-1]:
        #print(q)
        #print(f"{q%1000}")
        if q%10000>1000 and q%10000 < 2000:
            #print(q)
            if q%10 < 3 or (q%10 == 3 and q % 100 < 10):
                k += 1
                #print(q)
                if q%100>25:
                    print(f"a){q}")
                    print(f"b){k}")
                    break