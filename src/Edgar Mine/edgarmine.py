from math import*
S,N,W=map(int,input().split());G=[(S,S)]
for _ in'.'*N:
 E,H,L=map(float,input().split());K=L/4/pi/W-H*H
 if K>0:G+=[(E-sqrt(K),E+sqrt(K))]
G.sort();s=z=i=0;e=-1
while i<len(G):
 if G[i][0]<=s:e=max(e,G[i][1]);i+=1
 else:
  s=e;z+=1
  if e<G[i][0]or e>=S:break
print(z)