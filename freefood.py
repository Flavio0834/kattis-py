N=int(input())

somme=0
days=[]
for k in range(365):
    days.append(0)

for i in range(N):
    s,t=map(int,input().split())
    for j in range(s,t+1):
        if days[j-1]<1:
            days[j-1]=1

print(int(sum(days)))