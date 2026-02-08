import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from array import *
K = len(S:=[x-97 for x in input().strip()]); N, Q = map(int, input().split()); D = sorted(input().strip() for _ in range(N)); I = [[] for _ in range(26)]; Z = array('h', [-1]*26*(K+1)); R = [[] for _ in range(K*K)]; O = ['NO SUCH WORD']*Q; P = [[] for _ in range(K*K)]
for i in range(K): I[S[i]].append(i)
for i in range(26):
    u = 26*~-K+i
    for j in range(K-1, -1, -1):
        if S[j] == i: Z[u] = j
        else: Z[u] = Z[u+26]
        u -= 26
for i in range(Q): l, r, k = map(int, input().split()); R[~-l*K+r-1].append((k, i))
for i in range(N):
    n = len(s:=D[i]); c = 0
    if n>K: continue
    for a in I[s[0]-97]:
        b = a; ok = 1
        for j in range(1, n):
            b = Z[26*b+s[j]-71]
            if b < 0: ok = 0; break
        if ok:
            for j in range(c, a+1): P[j*K+b].append(i)
            c = a+1

class FenwickTree:
    def __init__(self, n):
        self.n = n; self.ft = array('I', [0]*-~n)
    def add(self, idx):
        idx += 1
        while idx <= self.n: self.ft[idx] += 1; idx += idx&(-idx)
    def kth(self, k):
        x = idx = 0; f = self.ft; n = self.n
        for i in range(14, -1, -1):
            if (t:=idx|(1<<i)) <= n and f[t] < k: k -= f[idx:=t]
        return idx

ft = FenwickTree(N); t = ft.ft; a = ft.add; g = ft.kth
for i in range(K*K):
    if i%K<1:
        c = 0
        for j in range(-~N): t[j] = 0
    for p in P[i]: a(p); c += 1
    for k, l in R[i]:
        if k <= c: O[l] = ''.join(map(chr, D[g(k)][:10]))
sys.stdout.write('\n'.join(O))