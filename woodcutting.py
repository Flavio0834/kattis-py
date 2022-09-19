T = int(input())
for t in range(T):
    N = int(input())
    times = []
    for i in range(N):
        woods = list(map(int, input().split()))
        Wi = woods.pop(0)
        times.append(sum(woods))
    times.sort()
    for i in range(1, len(times)):
        times[i] += times[i - 1]
    print(sum(times) / len(times))
