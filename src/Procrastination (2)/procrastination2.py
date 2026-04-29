def knapsack(capacity, vals, weights):
    n = len(vals)
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,capacity+1):
            if j >= weights[i-1]: dp[i][j] = max(dp[i-1][j-weights[i-1]]+vals[i-1], dp[i-1][j])
            else: dp[i][j] = dp[i-1][j]
    return dp

n, t = input().split()
h, m, s = map(int, t.split(':'))
capacity = 3600*h+60*m+s+60
vals, weights = [], []
for _ in range(int(n)):
    tt, vv = input().split(); vals.append(int(vv))
    hh, mm, ss = map(int, tt.split(':'))
    weights.append(3600*hh+60*mm+ss+60)
print(max(map(max, knapsack(capacity, vals, weights))))