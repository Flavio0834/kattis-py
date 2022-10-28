G, T, N = map(int, input().split())
Lw = list(map(int, input().split()))
W = sum(Lw)

print(int(0.9 * (G - T) - W))
