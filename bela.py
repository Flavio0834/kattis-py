A=[11,11]
K=[4,4]
Q=[3,3]
J=[20,2]
T=[10,10]
Neuf=[14,0]
Huit=[0,0]
Sept=[0,0]
N,B=input().split()
N=int(N)
res=0

for i in range(4*N):
    x=input()
    if x[1]==B:
        k=0
    else:
        k=1
    res+=A[k] if x[0]=='A' else K[k] if x[0]=='K' else Q[k] if x[0]=='Q' else J[k] if x[0]=='J' else T[k] if x[0]=='T' else Neuf[k] if x[0]=='9' else Huit[k] if x[0]=='8' else Sept[k]
print(res)