N = int(input())
for i in range(N):
    input()
    N = int(input())
    candies = 0
    for i in range(N):
        candies += int(input())
    print("YES" if candies % N == 0 else "NO")
