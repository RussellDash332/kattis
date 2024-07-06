def make_sa(s):
    n = len(s)
    sa = list(range(n))
    ra = [ord(s[i]) for i in range(n)]
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
    return [0]+lcp

# https://stackoverflow.com/questions/31106459/how-to-adapt-fenwick-tree-to-answer-range-minimum-queries/34602284#34602284
def update(a, i, x):
    a[i] = x
    while i > 1: i //= 2; a[i] = min(a[2*i], a[2*i+1])
def rmq(a, i, j):
    x = 10**6
    while i < j:
        if i%2 == 0: i //= 2
        else: x = min(x, a[i]); i = i//2 + 1
        if j%2 == 0: j //= 2
        else: x = min(x, a[j-1]); j //= 2
    return x

import sys; input = sys.stdin.readline
while (n:=int(input())):
    w = [input().strip() for _ in range(n)]
    if n == 1: print(w[0]); continue
    s = ''; m = []
    for i in range(n): s += w[i]+chr(i+1); m.extend([i]*(len(w[i])+1))
    N = len(s); sa = make_sa(s+'\0'); lcp = make_lcp(s, sa); r = [m[sa[i]] for i in range(N)]; cnt = [0]*n
    # whenever it includes {target} substrings, get min LCP among all included LCPs
    target = n//2+1; lo = 0; inc = 1; cnt[r[0]] = 1; a = [10**6]*2*N; best = (-1, []); has_hi = 0
    for hi in range(1, N):
        cnt[r[hi]] += 1; inc += cnt[r[hi]] == 1; update(a, hi+N, lcp[hi])
        while inc == target: # just need one substring for a fixed end
            b = rmq(a, lo+N, hi+1+N)
            if b > best[0]: best = (b, [lo]); has_hi = 1
            elif b == best[0] and not has_hi: best[1].append(lo); has_hi = 1
            elif b < best[0]: has_hi = 0
            cnt[r[lo]] -= 1; inc -= cnt[r[lo]] == 0
            lo += 1; update(a, lo+N, 10**6)
    if best[0]:
        for i in best[1]: print(s[sa[i]:sa[i]+best[0]])
    else: print('?')
    print()