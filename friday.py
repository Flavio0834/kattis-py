T=int(input())

for i in range(T):
    D,M=map(int,input().split())
    jparm=list(map(int,input().split()))
    cpt=0
    for j in range(M):
        type=0
        for k in range(j):
            type+=jparm[k]
        if jparm[j]>=13:
            type+=13
            type=type%7
            if type==6:
                cpt+=1
    print(cpt)




