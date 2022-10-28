t, s, n = map(int, input().split())
L = list(map(int, input().split()))
L.append(t)

side = 1
low = s
high = 0
for i in range(1, len(L)):
    side = not side
    dt = L[i] - L[i - 1]
    if side == 0:
        if dt > low:
            high += low
            low = 0
        else:
            high += dt
            low -= dt
    else:
        if dt > high:
            low += high
            high = 0
        else:
            low += dt
            high -= dt

print(high if side else low)
