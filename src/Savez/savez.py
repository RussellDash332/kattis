P=31;M=10**9+7;H={};N=int(input());G=[[]for _ in'.'*N]
for i in range(N):
 h=[z:=0];Z=0
 for c in input():h+=[z:=(z*P+ord(c))%M]
 for l in range(1,len(h)):
  if h[l]in H and(z-h[~l]*pow(P,l,M))%M==h[l]:Z=max(Z,H[h[l]])
 H[z]=max(H.get(z,0),Z+1)
print(max(H.values()))