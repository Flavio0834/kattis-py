L=[]
for i in range(10):
    a=int(input())
    if a%42 not in L:
        L.append(a%42)
print(len(L))