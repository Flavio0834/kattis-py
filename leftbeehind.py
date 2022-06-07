sw,so=map(int,input().split())
while (sw,so)!=(0,0):
    print("Never speak again." if sw+so==13 else "Left beehind." if sw<so else "To the convention." if sw>so else "Undecided.")
    sw,so=map(int,input().split())