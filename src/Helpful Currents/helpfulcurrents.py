import sys; input = sys.stdin.readline; from array import *
r, c, x = map(int, input().split()); m = ''.join(input().strip() for _ in range(r)); s = (r-1)*c+x
for tt in range(r*c):
    if m[tt] == '@': break
v = array('b', ii:=[0]*r*c); dp = array('i', ii); dp[tt] = 1; M = 10**6+3; ss = [2*s]
while ss:
    ub = ss.pop(); u, b = ub//2, ub%2
    if b:
        if m[u] == '<' and m[u-1] > '#': dp[u] += dp[u-1]
        elif m[u] == '>' and m[u+1] > '#': dp[u] += dp[u+1]
        if u >= c and m[u-c] > '#': dp[u] += dp[u-c]
        dp[u] %= M
    elif v[u] == 0:
        v[u] = 1; ss.append(2*u+1)
        if m[u] == '<' and v[u-1] == 0 and m[u-1] > '#': ss.append(2*u-2)
        elif m[u] == '>' and v[u+1] == 0 and m[u+1] > '#': ss.append(2*u+2)
        if u >= c and v[u-c] == 0 and m[u-c] > '#': ss.append(2*(u-c))
print(dp[s] if v[tt] else 'begin repairs')