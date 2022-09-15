n, m = map(int, input().split())
rankings = [i + 1 for i in range(n)]
for k in range(m):
    i, j = input().split()
    i, j = i[1], j[1]

    ii = rankings.index(int(i))
    ji = rankings.index(int(j))

    if ii > ji:
        rankings = (
            rankings[:ji] + rankings[ji + 1 : ii + 1] + [int(j)] + rankings[ii + 1 :]
        )

for i in range(len(rankings)):
    rankings[i] = "T" + str(rankings[i])

print(*rankings)
