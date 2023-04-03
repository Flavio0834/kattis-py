n = int(input())
C = sorted(list(map(int, input().split())))

k = n
mini = 1
possible = True
for i in range(n):
    if C[-1] > k:
        possible = False
        break
    else:
        x = C[-1] / k
        C.pop()
        k -= 1
        if x <= mini:
            mini = x

if possible:
    print(mini)
else:
    print("impossible")
