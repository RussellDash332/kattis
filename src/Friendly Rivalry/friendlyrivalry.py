def f(d):
    g = [[] for _ in range(2*n)]; c = [0]*2*n; s = []; e = 0; v = n; dp = [0]*(2*n+1); dp[0] = 1; z = set()
    for i in range(2*n):
        for j in range(i):
            if (X[i]-X[j])**2 + (Y[i]-Y[j])**2 < d: g[i].append(j); g[j].append(i)
    for i in range(2*n):
        if c[i] == 0:
            e += 1; q = [i]; w = 0
            while q:
                u = q.pop()
                if c[u] == 0: c[u] = e; w += 1; q.extend(g[u])
            s.append(w)
    for i in range(1, len(s)+1):
        for j in range(2*n, 0, -1):
            if j >= s[i-1] and dp[j-s[i-1]]%2: dp[j] = dp[j-s[i-1]]|(1<<i)
    if dp[n]%2: return [i+1 for i in range(2*n) if dp[n]&(1<<c[i])]
n = int(input()); X = []; Y = []
for _ in range(2*n): x, y = map(int, input().split()); X.append(x); Y.append(y)
D = sorted({(X[i]-X[j])**2 + (Y[i]-Y[j])**2 for i in range(2*n) for j in range(i)}); lo, hi = 0, len(D)-1
while hi-lo>1:
    if f(D[mi:=(lo+hi)//2]): lo = mi
    else: hi = mi-1
ans = D[hi] if f(D[hi]) else D[hi-1]; print(ans**.5, *f(ans))