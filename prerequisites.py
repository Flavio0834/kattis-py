entree=input()
while entree!='0':
    validite=1
    k,m=map(int,entree.split())
    A=list(map(int,input().split()))
    for i in range(m):
        B=list(map(int,input().split()))
        r,c=B[0],B[1]
        B.pop(0)
        B.pop(0)
        cpt=0
        for x in A:
            if x in B:
                cpt+=1
        if cpt<c:
            validite=0
    print("yes" if validite==1 else "no")
    entree=input()