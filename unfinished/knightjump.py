import copy


def pcc(nums, x, y, n):
    nums[x][y] = min(nums[x][y], n + 1)
    return nums[x][y]


if __name__ == "__main__":
    N = int(input())
    L = []
    K = 0, 0
    deltas = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    for i in range(N):
        L.append(list(input()))
        if "K" in L[-1]:
            K = i, L[-1].index("K")

    nums = []
    for i in range(N):
        a = []
        for j in range(N):
            if L[i][j] == ".":
                a.append(float("inf"))
            else:
                a.append(L[i][j])
        nums.append(a)

    queue = [(*K, 0)]
    x, y = -1, -1
    visited = set()
    while queue != [] and (x, y) != (0, 0):
        x, y, n = queue.pop(0)
        if (x, y) != K:
            n = pcc(nums, x, y, n)

        if (
            (x, y) == (0, 0)
            or (
                nums[x][y] != float("inf")
                and type(nums[x][y]) is not str
                and nums[x][y] < n
            )
        ) and K in visited:
            continue
        visited.add((x, y))

        for delta in deltas:
            x1 = x + delta[0]
            y1 = y + delta[1]
            if (
                (x1, y1) not in visited
                and x1 >= 0
                and x1 < N
                and y1 >= 0
                and y1 < N
                and (L[x1][y1] == "." or (x1, y1) == (0, 0))
            ):
                queue.append((x1, y1, n))

    print(nums[0][0] if nums[0][0] != float("inf") else -1)
