l=list(map(int,input().split()))
b=str(input())
res=[0,0,0]

l.sort()
for i in range(3):
    if b[i]=="A":
        res[i]=l[0]
    elif b[i]=="B":
        res[i]=l[1]
    else:
        res[i]=l[2]

print(str(res[0])+" "+str(res[1])+" "+str(res[2]))