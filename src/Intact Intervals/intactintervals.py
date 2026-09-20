_,X,Y=open(0);H={};h=T=10**9+7
for x,y in zip(X.split(),Y.split()):H[h]=H.get(h:=h+hash(x)-hash(y),0)+1
print(sum(~H[x]+2**H[x]for x in H)%T)