def dfs(node):
    if node not in visited:
        visited.add(node)
        for neighbour in bridges[node]:
            dfs(neighbour)


if __name__ == "__main__":
    N, M = map(int, input().split())
    bridges = {}
    for i in range(N):
        bridges[i + 1] = []
    for i in range(M):
        a, b = map(int, input().split())
        bridges[a].append(b)
        bridges[b].append(a)

    visited = set()
    dfs(1)
    print("YES" if len(visited) == N else "NO")
