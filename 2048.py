def clearing_line_left(L, i):
    for j in range(4):
        if L[i][0] == 0:
            L[i][0] = L[i][1]
            L[i][1] = L[i][2]
            L[i][2] = L[i][3]
            L[i][3] = 0
    for j in range(3):
        if L[i][1] == 0:
            L[i][1] = L[i][2]
            L[i][2] = L[i][3]
            L[i][3] = 0
    for j in range(2):
        if L[i][2] == 0:
            L[i][2] = L[i][3]
            L[i][3] = 0


def clearing_line_right(L, i):
    for j in range(4):
        if L[i][3] == 0:
            L[i][3] = L[i][2]
            L[i][2] = L[i][1]
            L[i][1] = L[i][0]
            L[i][0] = 0
    for j in range(3):
        if L[i][2] == 0:
            L[i][2] = L[i][1]
            L[i][1] = L[i][0]
            L[i][0] = 0
    for j in range(2):
        if L[i][1] == 0:
            L[i][1] = L[i][0]
            L[i][0] = 0


def clearing_col_up(L, j):
    for i in range(4):
        if L[0][j] == 0:
            L[0][j] = L[1][j]
            L[1][j] = L[2][j]
            L[2][j] = L[3][j]
            L[3][j] = 0
    for i in range(3):
        if L[1][j] == 0:
            L[1][j] = L[2][j]
            L[2][j] = L[3][j]
            L[3][j] = 0
    for i in range(2):
        if L[2][j] == 0:
            L[2][j] = L[3][j]
            L[3][j] = 0


def clearing_col_down(L, j):
    for i in range(4):
        if L[3][j] == 0:
            L[3][j] = L[2][j]
            L[2][j] = L[1][j]
            L[1][j] = L[0][j]
            L[0][j] = 0
    for i in range(3):
        if L[2][j] == 0:
            L[2][j] = L[1][j]
            L[1][j] = L[0][j]
            L[0][j] = 0
    for i in range(2):
        if L[1][j] == 0:
            L[1][j] = L[0][j]
            L[0][j] = 0


if __name__ == "__main__":
    L = []

    for i in range(4):
        L.append(list(map(int, input().split())))

    move = int(input())

    if move == 0:
        # left
        for i in range(4):
            clearing_line_left(L, i)
            if L[i][0] == L[i][1]:
                L[i][0] = 2 * L[i][0]
                L[i][1] = L[i][2]
                L[i][2] = L[i][3]
                L[i][3] = 0

                if L[i][1] == L[i][2]:
                    L[i][1] = 2 * L[i][1]
                    L[i][2] = 0

            elif L[i][1] == L[i][2]:
                L[i][1] = 2 * L[i][1]
                L[i][2] = L[i][3]
                L[i][3] = 0

            elif L[i][2] == L[i][3]:
                L[i][2] = 2 * L[i][2]
                L[i][3] = 0

    elif move == 1:
        # up
        for j in range(4):
            clearing_col_up(L, j)
            if L[0][j] == L[1][j]:
                L[0][j] = 2 * L[0][j]
                L[1][j] = L[2][j]
                L[2][j] = L[3][j]
                L[3][j] = 0

                if L[1][j] == L[2][j]:
                    L[1][j] = 2 * L[1][j]
                    L[2][j] = 0

            elif L[1][j] == L[2][j]:
                L[1][j] = 2 * L[1][j]
                L[2][j] = L[3][j]
                L[3][j] = 0

            elif L[2][j] == L[3][j]:
                L[2][j] = 2 * L[2][j]
                L[3][j] = 0

    elif move == 2:
        # right
        for i in range(4):
            clearing_line_right(L, i)
            if L[i][3] == L[i][2]:
                L[i][3] = 2 * L[i][3]
                L[i][2] = L[i][1]
                L[i][1] = L[i][0]
                L[i][0] = 0

                if L[i][2] == L[i][1]:
                    L[i][2] = 2 * L[i][2]
                    L[i][1] = 0

            elif L[i][2] == L[i][1]:
                L[i][2] = 2 * L[i][2]
                L[i][1] = L[i][0]
                L[i][0] = 0

            elif L[i][1] == L[i][0]:
                L[i][1] = 2 * L[i][1]
                L[i][0] = 0

    else:
        # down
        for j in range(4):
            clearing_col_down(L, j)
            if L[3][j] == L[2][j]:
                L[3][j] = 2 * L[3][j]
                L[2][j] = L[1][j]
                L[1][j] = L[0][j]
                L[0][j] = 0

                if L[2][j] == L[1][j]:
                    L[2][j] = 2 * L[2][j]
                    L[1][j] = 0

            elif L[2][j] == L[1][j]:
                L[2][j] = 2 * L[2][j]
                L[1][j] = L[0][j]
                L[0][j] = 0

            elif L[1][j] == L[0][j]:
                L[1][j] = 2 * L[1][j]
                L[0][j] = 0

    for i in range(4):
        print(*L[i])
