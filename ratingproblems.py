n,k=map(int,input().split())
note=0
for i in range(n):
    if i<k:
        note+=int(input())
        maxi,mini=note,note
    elif i==k:
        maxi=note+3
        mini=note-3
    else:
        maxi+=3
        mini-=3
print(mini/n,maxi/n)