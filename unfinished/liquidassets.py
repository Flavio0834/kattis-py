n = int(input())
L = input().split()
vowels = "aeiouy"
L2 = []
for k in L:
    k2 = k[0]
    for i in range(1, len(k)):
        if k[i] != k[i - 1]:
            k2 += k[i]
    k3 = k2[0]
    for i in range(1, len(k2) - 1):
        if k2[i] not in vowels:
            k3 += k2[i]
    if len(k2) > 1:
        k3 += k2[-1]
    L2.append(k3)

print(*L2)
