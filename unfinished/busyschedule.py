x=int(input())
OH=False
while x!=0:
    if OH:
        print('')
    OH=True
    L=[]
    R=False
    for i in range(x):
        L.append(input())
    Lam=[]
    for i in range(len(L)):
        if 'a.m.' in L[i]:
            Lam.append(L[i])
    Lpm=[]
    for i in range(len(L)):
        if L[i] not in Lam:
            Lpm.append(L[i])
    for i in range(len(Lam)):
        dp=Lam[i].index(':')
        if dp==1:
            Lam[i]=(int(Lam[i][0]),int(Lam[i][2]+Lam[i][3]))
        else:
            Lam[i]=(int(Lam[i][0]+Lam[i][1]),int(Lam[i][3]+Lam[i][4]))
    for i in range(len(Lpm)):
        dp=Lpm[i].index(':')
        if dp==1:
            Lpm[i]=(int(Lpm[i][0]),int(Lpm[i][2]+Lpm[i][3]))
        else:
            Lpm[i]=(int(Lpm[i][0]+Lpm[i][1]),int(Lpm[i][3]+Lpm[i][4]))

    Lam.sort()
    Lpm.sort()
    for k in Lam:
        if 12 in k:
            if k[1]<10:
                mm='0'+str(k[1])
            else:
                mm=str(k[1])
            print('12:'+mm+' a.m.')
            Lam.pop(Lam.index(k))
    for k in Lam:
        if k[1]<10:
            mm='0'+str(k[1])
        else:
            mm=str(k[1])
        print(str(k[0])+':'+mm+' a.m.')

    for k in Lpm:
        if 12 in k:
            if k[1]<10:
                mm='0'+str(k[1])
            else:
                mm=str(k[1])
            print('12:'+mm+' p.m.')
            Lpm.pop(Lpm.index(k))

    for k in Lpm:
        if k[1]<10:
            mm='0'+str(k[1])
        else:
            mm=str(k[1])
        print(str(k[0])+':'+mm+' p.m.')


    x=int(input())