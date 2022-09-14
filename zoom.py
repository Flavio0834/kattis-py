n, k = map(int, input().split())
a = list(map(int, input().split()))

res = []
for i in range(len(a)):
    if (i + 1) % k == 0:
        res.append(a[i])

# print elements of the line seperated by spaces on one line
print(*res)
