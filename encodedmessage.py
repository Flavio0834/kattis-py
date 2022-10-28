import math

N = int(input())
for i in range(N):
    a = input()
    vN = int(math.sqrt(len(a)))
    L = []
    for j in range(vN):
        L.append(list(a[j * vN : (j + 1) * vN]))

    b = ""
    for i1 in range(vN):
        for j1 in range(vN):
            b += L[j1][vN - i1 - 1]

    print(L, b)
