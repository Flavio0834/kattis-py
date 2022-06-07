T=int(input())
for i in range(T):
    x=int(input())
    res=1
    for j in range(1,x+1):
        res=res*j
    print(res%10)

