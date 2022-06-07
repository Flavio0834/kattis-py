import math
N=int(input())
for i in range(N):
    v0,theta,x1,h1,h2=map(float,input().split())
    t=x1/(v0*math.cos(theta*math.pi/180))
    y=v0*t*math.sin(theta*math.pi/180)-9.81*(t**2)/2
    print("Safe" if y>h1+1 and y<h2-1 else "Not Safe")