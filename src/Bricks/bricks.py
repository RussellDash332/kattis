from functools import *
def rot(s): return [[s[~j][i] for j in range(len(s))] for i in range(len(s[0]))]
def tr(s):
    m = [0]*len(s[0])
    for i in range(len(s)):
        for j in range(len(s[0])): m[j] += s[i][j]<'_'
    while m[-1]<1: m.pop()
    for i in range(len(s)):
        if m[i]: return tuple(m[i:])
@cache
def dp(s, n):
    if n == N: return 0
    Z = 0
    for r in R[n]:
        for i in range(7-len(r)):
            t = [*s]; ok = 1; z = 0
            for j in range(len(r)):
                t[i+j] += r[j]
                if t[i+j] > 8: ok = 0; break
            if ok:
                for j in range(6):
                    if t[j] > 2: z += t[j]; t[j] = 0
                Z = max(dp(tuple(t), n+1)+z*P[n], Z)
    return Z
R = []; P = []
for _ in range(N:=int(input())): c, r, p = map(int, input().split()); P.append(p); A = [input() for _ in range(r)]; B = rot(A); C = rot(B); D = rot(C); R.append({*map(tr, (A, B, C, D))})
print(dp((0,)*6, 0))