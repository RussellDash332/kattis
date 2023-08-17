import sys; input = sys.stdin.readline
n, p = map(float, input().split()); n = round(n); capacity = round(p*10000)

def knapsack(capacity, vals, weights):
    # max sum(vals_p) with sum(weights_p) <= capacity
    n = len(vals)
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,capacity+1):
            if j >= weights[i-1]: dp[i][j] = max(dp[i-1][j-weights[i-1]]+vals[i-1], dp[i-1][j])
            else: dp[i][j] = dp[i-1][j]
    return dp[-1]

# we want min sum(vals_p) with sum(weights_p) >= capacity
# we can consider the complement q and run knapsack on q with sum(weights_q) <= 10000-capacity
vals = []; weights = []
for _ in range(n):
    e, p = map(float, input().split())
    if p: vals.append(round(e)), weights.append(round(p*10000))
print(sum(vals)-max(knapsack(10000-capacity, vals, weights)))