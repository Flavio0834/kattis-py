lalalala=[0]
lalalala.pop(0)

A=[]
for i in range(5):
    A.append(input())
validite=1
cpt=0
for i in range(5):
    for j in range(5):
        if A[i][j]=='k':
            cpt+=1
            if i+2<5:
                if j+1<5:
                    if A[i+2][j+1]=='k':
                        validite=0
                if j-1>=0:
                    if A[i+2][j-1]=='k':
                        validite=0
            if i-2>=0:
                if j+1<5:
                    if A[i-2][j+1]=='k':
                        validite=0
                if j-1>=0:
                    if A[i-2][j-1]=='k':
                        validite=0
            if j+2<5:
                if i+1<5:
                    if A[i+1][j+2]=='k':
                        validite=0
                if i-1>=0:
                    if A[i-1][j+2]=='k':
                        validite=0
            if j-2>=0:
                if i+1<5:
                    if A[i+1][j-2]=='k':
                        validite=0
                if i-1>=0:
                    if A[i-1][j-2]=='k':
                        validite=0

print("valid" if (validite==1 and cpt==9) else "invalid")