x=input()
a=0
b=3
P,K,H,T=[],[],[],[]
X=True
while b!=len(x)+3:
    y=x[a:b]
    if y in P+K+H+T:
        print('GRESKA')
        X=False
        break
    if y[0]=='P':
        P.append(y)
    elif y[0]=='K':
        K.append(y)
    elif y[0]=='H':
        H.append(y)
    else:
        T.append(y)
    a+=3
    b+=3
if X:
    print(13-len(P),13-len(K),13-len(H),13-len(T))