L=list(input().split())
liste=[0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(5):
    L[i]=L[i][:-1]

for k in L:
    if k=='A':
        liste[0]+=1
    elif k=='T':
        liste[9]+=1
    elif k=='J':
        liste[10]+=1
    elif k=='Q':
        liste[11]+=1
    elif k=='K':
        liste[12]+=1
    else:
        liste[int(k)-1]+=1

print(max(liste))