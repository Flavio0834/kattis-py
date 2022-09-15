L=["clank","bong","click","tap","poing","clonk","clack","ping","tip","cloing","tic","cling","bing","pong","clang","pang","clong","tac","boing","boink","cloink","rattle","clock","toc","clink","tuc"]
minus="abcdefghijklmnopqrstuvwxyz"
majus="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
shift=False
res=[]

N=int(input())
for i in range(N):
    k=input()
    if k=="whack":
        res.append(" ")
    elif k=="pop":
        res=res[:len(res)-1]
    elif k=="dink" or k=="thumb" or k=="bump":
        shift=not(shift)
    else:
        if shift==False:
            res.append(minus[L.index(k)])
        else:
            res.append(majus[L.index(k)])

print("".join(x for x in res))