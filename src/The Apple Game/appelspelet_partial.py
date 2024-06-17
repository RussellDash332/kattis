from array import *; n = int(input())
if n % 2 == 0: print('beata'); exit(0)
n //= 2; dp = array('i', [-1]*(n+7)); a = array('b', [0]*(n+7))

def mex(s):
    if not s: return 0
    for i in s: a[i] = 1
    for i in range(max(s)+2):
        if a[i] == 0:
            for j in s: a[j] = 0
            return i

# Sprague-Grundy
def g(n):
    if dp[n] != -1: return dp[n]
    s = set()
    for i in range((n-1)//2): s.add(g(i)^g(n-3-i))
    dp[n] = mex(s); return dp[n]

import sys; sys.setrecursionlimit(max(20000, n+100))
print(['alf', 'beata'][g(n) == g(n+1)])