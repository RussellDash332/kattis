import sys; input = sys.stdin.readline; from bisect import *
def merge(intervals): h=lambda a,b:0 if a[1]<b[0]or b[1]<a[0]else[min(a[0],b[0]),max(a[1],b[1])]; return [r:=[],[[r.pop(),r.append(k)]if r and(k:=h(r[-1],j))else r.append(j)for j in sorted(intervals)]][0]
P = []; I = []; Q = {}; N, M = map(int, input().split())
for _ in range(N-1): c, s, t = input().split(); P.append(c); I.append((int(s), int(t)))
P.append(input().strip())
for _ in range(M):
    c, x = input().split()
    if c not in Q: Q[c] = []
    Q[c].append(int(x))
if P[0] not in Q: print('No'); exit()
S = Q[P[0]]
for i in range(N-1):
    x = P[i+1]; s, t = I[i]; T = []; U = []
    if x not in Q: print('No'); exit()
    for u in S:
        p, q = bisect_left(Q[x], u+s), bisect(Q[x], u+t)-1
        if p <= q: T.append((p, q))
    for u, v in merge(T): U.extend(Q[x][u:v+1])
    S = U
print('YNeos'[not S::2])