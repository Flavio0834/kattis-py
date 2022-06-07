import string
N=int(input())
for i in range(N):
    lettres=set(string.ascii_lowercase)
    res=""
    phrase=str(input()).lower()
    for k in phrase:
        if k in lettres:
            lettres-=set(k)
    if lettres==set():
        print("pangram")
    else:
        for j in string.ascii_lowercase:
            if j in lettres:
                res+=j
        print("missing",res)