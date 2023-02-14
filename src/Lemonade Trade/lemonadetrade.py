import sys
from math import log, exp

dp = {'pink': 0}
input()
for line in sys.stdin:
    v, u, w = line.split()
    if v not in dp: dp[v] = -1e9
    if u in dp: dp[v] = max(dp[v], dp[u]+log(float(w)))
if 'blue' not in dp: print(0)
else: print(exp(min(dp['blue'], log(10))))