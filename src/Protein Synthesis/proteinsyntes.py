M = 10**9+7
P = 31
F = [f:=1]+[f:=f*P%M for _ in range(10**6)]
def get(l, r):
    return (H[r]-H[l]*F[r-l])%M
def hsh(S):
    H = [0]
    for i in S: p = H[-1]; c = ord(i); H.append((p*P+c)%M)
    return H

import sys; input = sys.stdin.readline
N = int(input())
S = input().strip(); H = hsh(S); D = [0]+[N]*N
L = {}
for _ in range(int(input())):
    s = input().strip()
    if len(s) > N: continue
    h = hsh(s)[-1]; n = len(s)
    if n not in L: L[n] = set()
    L[n].add(h)
for i in range(N):
    for l, w in L.items():
        if i+l > N: continue
        if get(i, i+l) in w: D[i+l] = min(D[i+l], D[i]+1)
print(D[N])