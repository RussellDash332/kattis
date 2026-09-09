N,T,*W=map(int,open(0).read().split());Z=S=sum(W);D=[1]+[0]*T
for w in sorted(W)[::-1]:
 z=next((x for x in range(max(0,T-S+1),min(w-S,0)+T+1)if D[x]),-1);S-=w
 if-1<z<Z-S:Z=z+S
 for i in range(T,w-1,-1):D[i]|=D[i-w]
print(Z)