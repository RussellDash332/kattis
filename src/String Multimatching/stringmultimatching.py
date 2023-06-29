# https://github.com/stevenhalim/cpbook-code/blob/master/ch6/sa_lcp.py
def suffix_array_construction(s):
    n = len(s)
    sa = list(range(n))
    ra = [ord(s[i]) for i in range(n)]
    k, maxi = 1, max(300, n)
    while k < n:
        for kk in [k, 0]: # count sort on k and 0 respectively
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
    return sa

def string_matching(s, p, sa):
    n = len(s)
    m, lo, hi = len(p), 0, n-1
    while lo < hi:
        mid = (lo+hi)//2
        if s[sa[mid]:sa[mid]+m] >= p: hi = mid
        else: lo = mid+1
    if s[sa[lo]:sa[lo]+m] != p: return (-1, -1)
    l, hi = lo, n-1
    while lo < hi:
        mid = (lo+hi)//2
        if s[sa[mid]:sa[mid]+m] > p: hi = mid
        else: lo = mid+1
    return (l, hi - (s[sa[hi]:sa[hi]+m] != p))

import sys
n = -1
for s in sys.stdin:
    if n == -1: n, pp = int(s), []
    elif len(pp) != n: pp.append(s.strip('\r\n'))
    else:
        s = s.strip('\r\n')+'\0'
        sa = suffix_array_construction(s)
        for p in pp:
            lo, hi = string_matching(s, p, sa)
            if lo+1 or hi+1:
                res, j = [], lo
                while j <= hi: res.append(sa[j]); j += 1
                print(*sorted(res))
        n = -1