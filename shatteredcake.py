W=int(input())
N=int(input())
res=0
for i in range(N):
    w,l=map(int,input().split())
    res+=w*l
print(int(res/W))