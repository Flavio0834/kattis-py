N, B, H, W = map(int, input().split())
prices = []
dispo = []
for i in range(H):
    prices.append(int(input()))
    dispo.append(list(map(int, input().split())))

prixmini = 999999
for i in range(H):
    test = False
    for j in range(W):
        if dispo[i][j] >= N:
            test = True
            break
    if test:
        prix = N * prices[i]
        if prix <= B:
            if prix <= prixmini:
                prixmini = prix

if prixmini == 999999:
    print("stay home")
else:
    print(prixmini)
