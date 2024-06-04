from collections import *
c = dict(zip('XAEIOU', range(-1, 5))); s = [c[i] for i in input().strip()]; n = len(s); a = [*map(int, input().split())]; _, *d = map(int, input().split())
for i in d: s[i-1] = -1; a[i-1] = 0
w = Counter(s); v = Counter(c[i] for i in input().strip() if c[i]>-1); t = [w[i]+v[i] for i in range(5)]; D = [[-1]*32 for _ in range(n)]
def dp(i, bm):
    global s, a
    if i == n: return 0 if bm == 31 else float('inf')
    if D[i][bm] != -1: return D[i][bm]
    ans = dp(i+1, bm)+a[i] # leave space i empty?
    for j in range(5):
        if bm&(1<<j) or i+t[j]>n: continue
        # want to put company j in spaces [i...i+t[i]-1]
        # need to move all the j's after this range in + move all non-j's inside this range out
        e = 0; O = []; old_s = [*s]; old_a = [*a]
        # apply changes
        for k in range(i, i+t[j]):
            if s[k] != j: e += a[k]; O.append((s[k], a[k]))
        for k in range(i+t[j], n):
            if s[k] == j: e += a[k]; ss, aa = O.pop(); s[k] = ss; a[k] = aa
        ans = min(ans, e+dp(i+t[j], bm^(1<<j)))
        # revert changes
        s = old_s; a = old_a
    D[i][bm] = ans; return ans
print(dp(0, 0))