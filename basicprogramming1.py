N, t = map(int, input().split())
A = list(map(int, input().split()))

if t == 1:
    print(7)
elif t == 2:
    # if A[0] == A[1]:
    #     print("Equal")
    # else:
    print("Bigger" if A[0] > A[1] else "Equal" if A[0] == A[1] else "Smaller")
elif t == 3:
    print(sorted(A[:3])[1])
elif t == 4:
    print(sum(A))
elif t == 5:
    print(sum([i for i in A if i % 2 == 0]))
elif t == 6:
    A = [k % 26 for k in A]
    print("".join([chr(97 + i) for i in A]))
elif t == 7:
    i = 0
    visited = [False] * N
    while True:
        visited[i] = True
        i = A[i]
        if i >= N:
            print("Out")
            break
        elif i == N - 1:
            print("Done")
            break
        elif visited[i]:
            print("Cyclic")
            break
