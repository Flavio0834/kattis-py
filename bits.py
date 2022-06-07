T=int(input())

for i in range(T):
    res=0
    X=input()
    mot=''
    for x in X:
        mot+=x
        res1=0
        for k in bin(int(mot)):
            res1+=1 if k=='1' else 0
        res=res1 if res1>res else res
    print(res)

