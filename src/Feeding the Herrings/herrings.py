M=12345647;Z=range;X=[]
for s in Z(10):
 for l in Z(10):
  for k in Z(3):
   for t in Z(8):
    p,q,r=[{*Z(l*(i^1),10)}-{3}for i in(t>>2,t//2%2,t&1)];U=[0]*24
    for a in p:
     for b in q:
      for c in r:
       n=10*k-a-b-c+s
       if 0<=n<3:U[8*n+(t|(a>l)<<2|(b>l)<<1|(c>l))]+=1
    X+=[U]
for _ in Z(int(input())):
 S,L=input().split();N=len(S:=[*map(int,S)]);L=[0]*(N-len(L))+[*map(int,L)];D=[0]*-~N*24
 for i in Z(N,-1,-1):
  for w in Z(24):
   u=24*i+w
   if i<N:
    U=X[240*S[i]+24*L[i]+w]
    for j in Z(24):D[u]=(D[u]+D[u+24-u%24+j]*U[j])%M
   else:D[u]=w<8
 print(D[0])