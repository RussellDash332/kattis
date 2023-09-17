n = int(input()); s = str(n); m = {}
def bt(idx, curr):
    if idx == len(s): return curr == n
    if curr > n: return 0
    if (idx, curr) in m: return m[(idx, curr)]
    r = p = 0; d = int(s[idx])
    while curr+d**p <= n: r += bt(idx+1, curr+d**p); p += 1
    m[(idx, curr)] = r; return r
print(bt(0, 0))