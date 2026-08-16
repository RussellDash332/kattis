from collections import *
H, W, K, *C = map(int, open(0).read().split()); P = 3*10**5
Z = [0]*W; p = 0; A0 = []; A1 = []; B0 = []; B1 = []; C0 = []; C1 = []; D0 = []; D1 = []
for i in C: h = Z[i-1]; Z[i-1] += 1; (A0, A1)[p].append(h*P+i-1); (B0, B1)[p].append((i-1)*P+h); (C0, C1)[p].append((h-i+1)*P+h); (D0, D1)[p].append((h+i-1)*P+h); p ^= 1
T = []
for x, p in enumerate((A0, B0, C0, D0, A1, B1, C1, D1)):
    t = {e:i for i,e in enumerate(p)}; s = sorted(p); z = 10**9; q = deque()
    for i in range(len(p)):
        while q and q[0] <= i-K: q.popleft()
        while q and t[s[q[-1]]] <= t[s[i]]: q.pop()
        q += [i]
        if i >= K-1 and s[i]-s[i-K+1] == K-1: z = min(z, t[s[q[0]]])
    T += [(2*z+1+x//4, 'AB'[x//4])]
w, p = min(T)
if w < 10**9: print(p, w)
else: print('D')