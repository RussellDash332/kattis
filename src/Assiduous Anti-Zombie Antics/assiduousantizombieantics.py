def knapsack(capacity, vals, weights):
    n = len(vals)
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,capacity+1):
            if j >= weights[i-1]: dp[i][j] = max(dp[i-1][j-weights[i-1]]+vals[i-1], dp[i-1][j])
            else: dp[i][j] = dp[i-1][j]
    return dp
b, n = map(int, input().split())
B = [[*map(int, input().split())] for _ in range(b)]
vals = []; weights = []; W = V = 0; Z = []
for _ in range(n):
    s, w, v = input().split(); w = int(w); v = int(v)
    if s[0] == '*': W += w; V += v
    else: vals.append(v); weights.append(w)
for i in range(b):
    c, a = B[i]
    if W > c: continue
    d = knapsack(c-W, vals, weights)[-1]; m = d[-1]; k = d.index(m); Z.append((m+a+V, -k-W, -i))
if Z: x, y, z = max(Z); x>0 and print(-z, -y, x)!=exit()
print('Your sacrifice will be remembered')