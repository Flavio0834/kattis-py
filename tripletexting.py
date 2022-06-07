msg=input()
x=int(len(msg)/3)
msg1,msg2,msg3=msg[0:x],msg[x:2*x],msg[2*x:3*x]

y=True
while y:
    if msg1==msg2 or msg1==msg3:
        print(msg1)
        y=not y
    else:
        print(msg2)
        y=not y