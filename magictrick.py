mot=list(input())
l=len(mot)
L=[]
for i in range(l):
    if mot[-1] not in L:
        L.append(mot[-1])
        mot.pop()

print(1 if mot==[] else 0)