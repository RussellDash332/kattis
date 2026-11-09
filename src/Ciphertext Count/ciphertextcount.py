def make_sa(s):
    n = len(s)
    sa = list(range(n))
    ra = [*s]
    k, maxi = 1, max(300, n)
    while k < n:
        for kk in [k, 0]:
            c = [0]*maxi
            for i in range(n): c[ra[i+kk] if i+kk<n else 0] += 1
            ss, temp = 0, [0]*n
            for i in range(maxi): t = c[i]; c[i] = ss; ss += t
            for i in range(n):
                idx = ra[sa[i]+kk] if sa[i]+kk < n else 0
                temp[c[idx]] = sa[i]
                c[idx] += 1
            sa = temp
        temp, r = [0]*n, 0
        temp[sa[0]] = r
        for i in range(1, n):
            r += ra[sa[i]] != ra[sa[i-1]] or ra[sa[i]+k] != ra[sa[i-1]+k]
            temp[sa[i]] = r
        ra = temp
        if ra[sa[n-1]] == n-1: break
        k *= 2
    return sa[1:]

def make_lcp(s, sa):
    n = len(s)
    ra = [0]*n
    for i in range(n): ra[sa[i]] = i
    k = 0
    lcp = [0]*(n-1)
    for i in range(n):
        if ra[i] == n-1: k = 0; continue
        j = sa[ra[i]+1]
        while i + k < n and j + k < n and s[i+k] == s[j+k]: k += 1
        lcp[ra[i]] = k
        if k: k -= 1
    return [0]+lcp, ra

from array import *
MOD = 998244353
L = {}; S = []; N = len(s:=input())
for i, e in enumerate(s): S += [i-L[e]+1 if e in L else 1]; L[e] = i
lcp, rk = make_lcp(S, sa:=make_sa(S+[0]))

T = [[*lcp]]; B = 1
for _ in range(N.bit_length()-1): T.append([min(T[-1][j], T[-1][j+B]) for j in range(N+1-2*B)]); B <<= 1
def lce(i, j):
    if i == j: return N-i
    a, b = rk[i], rk[j]
    if a > b: a, b = b, a
    return min(T[k:=(b-a).bit_length()-1][a+1], T[k][b+1-(1<<k)])

fi = array('I', [N])*26*N; nx = [N]*26; ps = [*range(26)]
for i in range(N-1, -1, -1):
    c = ord(s[i])-97; nx.pop(q:=ps[c]); nx.insert(0, i)
    for j in range(26):
        fi[26*i+j] = nx[j]
        if j == c: ps[j] = 0
        else: ps[j] += ps[j]<q
def lcp2(i, j): # correction?
    if i == j: return N-i
    x = c = 0; m = N-max(i, j)
    while x < m:
        z = min(u:=fi[26*i+c]-i if c<26 else N-i, v:=fi[26*j+c]-j if c<26 else N-i, m)
        if x < z:
            d = lce(i+x, j+x)
            if d < z-x: return x+d
        x = z
        if x == m or u != v: return x
        c += 1; x += 1
    return x

from functools import *
def cmp(i, j):
    x = lcp2(i, j)
    if x == N-max(i, j): return (i<j)-(i>j)
    u = S[i+x] if S[i+x]<=x+1 else 1; v = S[j+x] if S[j+x]<=x+1 else 1
    return (u>v)-(u<v)

W = [1]*27
for k in range(1, 27): W[k] = W[k-1]*(27-k)%MOD
Z = 0; la = -1
for i in sorted(range(N), key=cmp_to_key(cmp)):
    st = lcp2(i, la)+1 if ~la else 1; la = i; k = 0
    for j in range(26):
        p = fi[26*i+j]
        if p == N: break
        p -= i
        if p >= st: Z += (p-st+1)*W[k]; st = p+1
        k += 1
    Z += (N-i-st+1)*W[k]
print(Z%MOD)