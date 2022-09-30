i = 0
while True:
    try:
        i += 1
        a, b = map(int, input().split())
        c, d = map(int, input().split())
        input()
        if a == 1 and b == 0 and c == 0 and d == 1:
            print(f"Case {i}:")
            print("1 0")
            print("0 1")
            continue
        print(f"Case {i}:")
        print(
            int(-1 * d / (c * (b - (a * d / c)))), int(-1 * b / (a * (d - (c * b / a))))
        )
        print(int(1 / (b - (a * d / c))), int(1 / (d - (c * b / a))))
    except:
        break
