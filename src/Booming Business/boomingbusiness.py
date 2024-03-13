from array import *
h, w = map(int, input().split()); M = 10**9+7; w += 1; h += 1
dp = array('i', [0]*w*h)
for i in range(h): dp[h+i] = 1
for i in range(2, w):
    for j in range(2, h):
        for k in range(1, i): dp[h*i+j] = (dp[h*i+j]+dp[h*k+j-1]*dp[h*(i-k)+j])%M
dp[h] = 0; print((dp[-1]-dp[-2])%M)