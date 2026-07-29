from itertools import*;S=input();K=len({*S});Z=1e9
for p in permutations({*S}):
 D=[0]*-~K
 for s in S:D=[v:=1e9]+[v:=min(D[k+1]+(s!=p[k]),v)for k in range(K)]
 Z=min(Z,D[K])
print(Z)