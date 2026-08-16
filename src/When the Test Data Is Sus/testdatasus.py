I=lambda:[*map(int,input().split())];N,C=I();D=[S:=0]*-~C
for v,w in sorted([I()for _ in'.'*N],key=lambda x:-x[0]/x[1])[:800]:
 for i in range(C-w,-1,-1):D[i+w]=max(D[i+w],D[i]+v)
print(max(D))