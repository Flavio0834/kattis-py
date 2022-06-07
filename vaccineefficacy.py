N=int(input())
vac=[0,0,0]
ctrl=[0,0,0]
nbvac=0
nbctrl=0

for i in range(N):
    x=input()
    if x[0]=='Y':
        nbvac+=1
        for j in range(1,4):
            if x[j]=='Y':
                vac[j-1]+=1
    else:
        nbctrl+=1
        for j in range(1,4):
            if x[j]=='Y':
                ctrl[j-1]+=1

for i in range(3):
    vac[i]=vac[i]*100/nbvac
    ctrl[i]=ctrl[i]*100/nbctrl
    if vac[i]>=ctrl[i]:
        print('Not Effective')
    else:
        print((ctrl[i]-vac[i])*100/ctrl[i])