N=int(input())
while N!=-1:
    dist=0
    temps=0
    for i in range(N):
        v,t=map(int,input().split())
        dist+=v*(t-temps)
        temps=t
    print(dist,"miles")
    N=int(input())