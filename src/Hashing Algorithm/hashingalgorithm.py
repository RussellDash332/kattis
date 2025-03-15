def make_sa(s):
    n = len(s)
    sa = list(range(n))
    ra = [ord(s[i])-96 for i in range(n)]
    k, maxi = 1, max(30, n)
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
    return [0]+lcp

def update(i, x):
    i += n; A[i] = x
    while i > 1: i >>= 1; A[i] = max(A[i<<1], A[(i<<1)+1])
def query(i, j):
    i += n; j += n; x = -10**18
    while i < j:
        if (i^1)&1: i >>= 1
        else: x = max(x, A[i]); i = (i>>1)+1
        if (j^1)&1: j >>= 1
        else: x = max(x, A[j-1]); j >>= 1
    return -x

import sys; input = sys.stdin.readline; M = 998244353
for _ in range(int(input())):
    s = input().strip(); lcp = make_lcp(s, sa:=make_sa(s+chr(96))); D = [(1, n:=len(s), 0)]; Z = 0; A = [-10**18]*2*n
    for i in range(n): update(i, -(n*lcp[i]+i))
    while D:
        l, r, u = D.pop()
        if l == r: Z += n-sa[l-1]-u; continue
        v, p = divmod(query(l, r), n); Z = (Z+(r-l+1)**2*(v-u))%M; D.append((l, p, v)); D.append((p+1, r, v))
    print(Z)