L=["clank","bong","click","tap","poing","clonk","clack","ping","tip","cloing","tic","cling","bing","pong","clang","pang","clong","tac","boing","boink","cloink","rattle","clock","toc","clink","tuc"]
minus="abcdefghijklmnopqrstuvwxyz"
majus="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
shift=False
res=[]

N=int(input())
for i in range(N):
    k=input()
    if k in L:
        if shift==False:
            res.append(minus[L.index(k)])
        else:
            res.append(majus[L.index(k)])
    else:
        if k=="whack":
            res.append(" ")
        elif k=="pop":
            res.pop()
        elif k=="dink" or k=="thumb" or k=="bump":
            shift=not(shift)

res1=""
for x in res:
    res1+=x
print(res1)