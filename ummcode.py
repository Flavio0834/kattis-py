L=input().split()
lettres='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnopqrstvwxyz'

M=[[]]
for i in range(len(L)):
    oui=True
    for x in lettres:
        if x in L[i]:
            oui=False
    if oui:
        for k in L[i]:
            if k=='u':
                if len(M[-1])<7:
                    M[-1]+='1'
                else:
                    M.append('1')
            elif k=='m':
                if len(M[-1])<7:
                    M[-1]+='0'
                else:
                    M.append('0')
res=''
for k in M:
    k=''.join(k)
    res+=chr(int('0b'+k,2))
print(res)