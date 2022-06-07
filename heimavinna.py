A=list(input().split(';'))
res=0
for i in range(len(A)):
    if '-' in A[i]:
        A[i]=list(map(int,A[i].split('-')))
        for j in range(A[i][0],A[i][1]+1):
            res+=1
    else:
        res+=1
print(res)