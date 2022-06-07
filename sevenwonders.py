x=input()
print(x.count('T')**2+x.count('C')**2+x.count('G')**2+7*min(x.count('T'),x.count('C'),x.count('G')))