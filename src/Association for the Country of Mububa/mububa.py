import sys; input = sys.stdin.readline
from bisect import *; from array import *
n = int(input()); a = [*map(int, input().split())]; cs = array('q', [0]); dp = [array('i', [0]*(n+2)) for _ in range(n+2)]
for i in a: cs.append(cs[-1]+i)
for i in range(n, -1, -1):
    for j in range(n, i, -1): dp[i][j] = max(dp[i][j+1], dp[j][(bisect_left(cs, m+cs[j-1]) or 1)+1]+1 if cs[n]-(cs[j-1] if j else 0) >= (m:=cs[j-1]-(cs[i-1] if i else 0)) else 0)
print(dp[0][1])