import string

N=int(input())
couleurs=[]
tailles=[]
for i in range(N):
    a,b=input().split()
    if b[0] in string.ascii_lowercase:
        a=int(a)/2
        tailles.append(a)
        couleurs.append(b)
    else:
        tailles.append(int(b))
        couleurs.append(a)

while tailles!=[]:
    print(couleurs[tailles.index(min(tailles))])
    couleurs.pop(tailles.index(min(tailles)))
    tailles.pop(tailles.index(min(tailles)))