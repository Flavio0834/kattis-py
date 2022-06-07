N=int(input())
TB=0
LR=0
for j in range(N):
    epee=input()
    for i in range(4):
        if epee[i]=='0':
            if i==0 or i==1:
                TB+=1
            else:
                LR+=1
a=min(TB//2,LR//2)
print(a,TB-2*a,LR-2*a)