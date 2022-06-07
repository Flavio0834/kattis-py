import math
N,W,H=map(int,input().split())
for i in range(N):
    print("NE" if int(input())>math.sqrt(W**2+H**2) else "DA")