import sys

N, K = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))

dico = dict()
for k in L:
    if k not in dico:
        dico[k] = 1
    else:
        dico[k] += 1


for i in range(K):
    values = list(dico.values())
    keys = list(dico.keys())

    dico[keys[values.index(max(values))]] -= 1

values = list(dico.values())
print(max(values))
