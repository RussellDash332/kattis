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

def lrs(lcp):
    best = (1, '')
    for i in range(1, len(lcp)): best = min(best, (-lcp[i], s[sa[i]:][:lcp[i]]))
    return best[1]

s = input().strip()
sa = make_sa(s + '\0')
lcp = make_lcp(s, sa)
print(lrs(lcp))