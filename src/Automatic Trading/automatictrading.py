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
    x = 10**9
    while i < j:
        if i%2 == 0: i //= 2
        else: x = min(x, a[i]); i = i//2 + 1
        if j%2 == 0: j //= 2
        else: x = min(x, a[j-1]); j //= 2
    return x

import sys; input = sys.stdin.readline; from array import *
s = input().strip(); n = len(s); sa = make_sa(s+'\0'); lcp = make_lcp(s, sa); r = array('i', [0]*2*n); m = array('i', [0]*n)
for i in range(n): m[sa[i]] = i; update(r, i+n, lcp[i])
for _ in range(int(input())): a, b = map(int, input().split()); print(rmq(r, min(m[a], m[b])+n+1, max(m[a], m[b])+n+1))