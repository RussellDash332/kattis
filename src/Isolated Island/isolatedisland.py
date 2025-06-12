X=[]
for _ in'.'*int(input()):a,b,c,d=map(int,input().split());X+=[(a,b),(c,d)]
print('yneos'[all(X.count(x)%2<1for x in X)::2])