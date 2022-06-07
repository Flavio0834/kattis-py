L,H=map(int,input().split())
res=0
for x in range(L,H+1):
    y=True
    L=[]
    for k in str(x):
        L.append(int(k))
        if k=='0' or x%int(k)!=0:
            y=False
    y2=True
    for i in range(len(L)):
        for j in range(len(L)):
            if i!=j and L[i]==L[j]:
                y2=False
    if y and y2:
        res+=1
print(res)