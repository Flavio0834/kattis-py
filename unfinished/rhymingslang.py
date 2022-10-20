word = input()
a = int(input())
lists = []
for i in range(a):
    lists.append(input().split())
lists2 = []
for i in range(len(lists)):
    for j in range(len(lists[i])):
        if lists[i][j] in word:
            lists2.append(lists[i])
            break
b = int(input())
for i in range(b):
    phrase = input().split()
    rhyme = False
    for j in range(len(lists2)):
        for k in range(len(lists2[j])):
            if lists2[j][k] in phrase[-1]:
                rhyme = True
                break
        if rhyme:
            break
    print("YES" if rhyme else "NO")
