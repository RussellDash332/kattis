import sys; input = sys.stdin.readline
n, m = map(int, input().split()); SZ = 61
w = [[*map(int, input().strip())] for _ in range(n)]

def f(d, ww, k):
    h = set(); e = [*ww]; i = 0
    if k == 0: return [*e] if e >= d else None
    while i < m:
        if e[i] != d[i]:
            if k > 1: h.add(i); e[i] = d[i]; k -= 1
            else:
                prev = e[i]; e[i] = d[i]
                if e >= d: return [*e]
                elif e[i] < 9:
                    e[i] += 1
                    if e[i] == prev:
                        for j in range(i+1, m):
                            if e[j] != 0: e[j] = 0; return [*e]
                    return [*e]
                e[i] = prev; i -= 1
                if i == -1: return
                while e[i] == 9:
                    i -= 1
                    if i == -1: return
                e[i] += 1
                if i in h:
                    for j in range(i+1, m):
                        if e[j] != 0: e[j] = 0; return [*e]
                return [*e]
        i += 1
    return [*e]

dp = [[None]*SZ for _ in range(n+1)]; dp[0][0] = [0]*m
par = [[None]*SZ for _ in range(n+1)]; par[0][0] = -1
for i in range(1, n+1):
    for j in range(SZ):
        for k in range(j+1):
            d = dp[i-1][j-k]
            if d == None: continue
            if (e:=f(d, w[i-1], k)) == None: continue
            if (dp[i][j] != None and dp[i][j] > e) or dp[i][j] == None: dp[i][j] = e; par[i][j] = j-k
for i in range(SZ):
    if dp[n][i] != None: break
ci, cj = n, i; ans = []
while ci: ans.append(''.join(map(str, dp[ci][cj]))); cj = par[ci][cj]; ci -= 1
while ans: print(ans.pop())