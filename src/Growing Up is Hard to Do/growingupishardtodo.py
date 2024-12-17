from bisect import *
N, *A = map(int, open(0).read().split()); B = []; P = []; M = 10**9+7
for e in A:
    p = bisect(B, e-1, key=lambda x: x[-1][0])
    if p == len(B): P.append([0]); B.append([])
    u = P[p-1][-1]-P[p-1][bisect(B[p-1], -e, key=lambda x: -x[0])] if p else 1
    if B[p] and B[p][-1][0] == e: B[p][-1] = (e, u); P[p][-1] = (P[p][-2]+u)%M
    else: B[p].append((e, u)); P[p].append((P[p][-1]+u)%M)
print(sum(b[1] for b in B[-1])%M if B else 0)