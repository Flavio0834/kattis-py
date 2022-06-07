N=int(input())
res=0
for i in range(N):
    a,b=map(float,input().split())
    res+=a*b
print(round(res,3))
