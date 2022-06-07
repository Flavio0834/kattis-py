n=int(input())
socks=[]
anies=[]
for i in range(n):
    sock_type,sock_side,sock_num=input().split()
    sock={'type':sock_type,'side':sock_side,'num':int(sock_num)}
    if sock['side']=='any':
        anies.append(sock)
    else:
        socks.append(sock)

socks_drawed=dict()
score=0
impossible=1
fini=0
socks=sorted(socks,key=lambda sock:sock['num'])[::-1]
anies=sorted(anies,key=lambda sock:sock['num'])
while socks:
    sock=socks.pop(0)
    same_type=socks_drawed.get(sock['type'],sock['side'])
    if same_type==sock['side']:
        score+=sock['num']
        socks_drawed[sock['type']]=sock['side']
    else:
        impossible=0
while anies:
    sock=anies.pop(0)
    same_type=socks_drawed.get(sock['type'],'')
    if same_type!='':
        impossible=0
    else:
        score+=1
        if sock['num']>1:
            impossible=0
if not impossible and not fini:
    print(score+1)
    fini=1
if impossible and not fini:
    print('impossible')