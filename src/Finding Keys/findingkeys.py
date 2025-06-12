n, *a = map(int, open(0))
s = [int(a[i]<a[(i+1)%n]) for i in range(n)]

def make_sa(s):
    n = len(s)
    sa = list(range(n))
    ra = [ord(s[i]) for i in range(n)]
    k, maxi = 1, max(300, n)
    while k < n:
        for kk in [k, 0]:
            c = [0]*maxi
            for i in range(n): c[ra[(i+kk)%n]] += 1
            ss, temp = 0, [0]*n
            for i in range(maxi): t = c[i]; c[i] = ss; ss += t
            for i in range(n):
                idx = ra[(sa[i]+kk)%n]
                temp[c[idx]] = sa[i]
                c[idx] += 1
            sa = temp
        temp, r = [0]*n, 0
        temp[sa[0]] = r
        for i in range(1, n):
            r += ra[sa[i]] != ra[sa[i-1]] or ra[(sa[i]+k)%n] != ra[(sa[i-1]+k)%n]
            temp[sa[i]] = r
        ra = temp
        if ra[sa[n-1]] == n-1: break
        k *= 2
    return sa

def make_lcp(s, sa):
    ra = [0]*n
    for i in range(n): ra[sa[i]] = i
    k = 0
    lcp = [0]*(n-1)
    for i in range(n):
        if ra[i] == n-1: k = 0; continue
        j = sa[ra[i]+1]
        while k < n and s[(i+k)%n] == s[(j+k)%n]: k += 1
        lcp[ra[i]] = k
        if k: k -= 1
    return [0]+lcp

z = [-1]*n
s = ''.join(map(str, s))
sa = make_sa(s)
lcp = make_lcp(s, sa)
for x, i in enumerate(sa): z[i] = max(lcp[x], lcp[(x+1)%n])+1
if z == [n+1]*n: z = [-1]*n
print(*z)