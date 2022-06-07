C=float(input())
L=int(input())
res=0
for i in range(L):
    w,l=map(float,input().split())
    res+=w*l*C
print(round(res,8))