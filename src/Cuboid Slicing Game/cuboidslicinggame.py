from array import *
dp = array('i', [-1]*30000); a = array('b', [0]*30000)

def mex(s):
    for i in s: a[i] = 1
    for i in range(max(s)+2):
        if a[i] == 0:
            for j in s: a[j] = 0
            return i

# Sprague-Grundy
def win(x, y, z):
    if x < 1 or y < 1 or z < 1: return 0
    if dp[(t:=961*x+31*y+z)] != -1: return dp[t]
    s = []
    # for every cut combo XOR across all 8 cuboids
    for i in range(x//2+1):
        for j in range(y//2+1):
            for k in range(z//2+1): s.append(win(i, j, k)^win(i, j, z-k-1)^win(i, y-j-1, k)^win(i, y-j-1, z-k-1)^win(x-i-1, j, k)^win(x-i-1, j, z-k-1)^win(x-i-1, y-j-1, k)^win(x-i-1, y-j-1, z-k-1))
    dp[t] = mex(s); return dp[t]

p = input(); g = 0; n = int(input())
for _ in range(n): g ^= win(*map(int, input().split()))
print(['RUBEN', 'ALBERT'][(p=='ALBERT')^(g==0)])