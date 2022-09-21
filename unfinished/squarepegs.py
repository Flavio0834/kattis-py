from math import sqrt

N, M, K = map(int, input().split())
plots = sorted(list(map(int, input().split())))[::-1]
circ = list(map(int, input().split()))
sqr = list(map(int, input().split()))

for i in range(len(sqr)):
    sqr[i] *= sqrt(2)

houses = circ + sqr
houses = sorted(houses)[::-1]

for i in range(len(plots)):
    plots[i] = [plots[i], 0]

res = 0
for i in range(len(houses)):
    for j in range(len(plots)):
        if (not plots[j][1]) and plots[j][0] > houses[i]:
            plots[j][1] = 1
            res += 1

print(res)
