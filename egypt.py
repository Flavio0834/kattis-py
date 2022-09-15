a, b, c = sorted(map(int, input().split()))
while (a, b, c) != (0, 0, 0):
    print("right" if a**2 + b**2 == c**2 else "wrong")
    a, b, c = sorted(map(int, input().split()))
