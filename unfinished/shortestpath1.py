while True:
    n, m, q, s = map(int, input().split())
    if n == 0 and m == 0 and q == 0 and s == 0:
        break
    paths = [[] for o in range(n)]
    for i in range(m):
        u, v, w = map(int, input().split())
        paths[u].append((v, w))

    distances = [float("inf") for o in range(n)]
    distances[s] = 0

    visited = [0 for o in range(n)]
    queue = [s]

    while queue:
        node = queue.pop(0)
        visited[node] = 1
        for couple in paths[node]:
            if not visited[couple[0]]:
                queue.append(couple[0])
            if distances[couple[0]] > distances[node] + couple[1]:
                distances[couple[0]] = distances[node] + couple[1]

    for i in range(q):
        x = int(input())
        if distances[x] < float("inf"):
            print(distances[x])
        else:
            print("Impossible")
