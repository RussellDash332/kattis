from array import *
n, k, *a = map(int, open(0).read().split())
m = max(a)
pc = array('i', [0]*m*(n+1))
for i in range(1, n+1):
    pc[i*m+a[i-1]-1] += 1
    for j in range(m): pc[i*m+j] += pc[i*m-m+j]
dp = [0]*(n+1)
for pos in range(n-1, -1, -1):
    kn = []
    for i in range(m):
        # check if we can take >= k occurences of type i
        lo, hi = pos, n-1
        while lo < hi:
            if pc[(mi:=(lo+hi)//2)*m+m+i]-pc[pos*m+i] >= k: hi = mi
            else: lo = mi+1
        kn.append(lo)
    dp[pos] = dp[pos+1]+2*(k==1)
    for i in sorted(kn):
        z = 1
        for j in range(m):
            v = pc[i*m+m+j]-pc[pos*m+j]
            if 0 < v < k: z = 0; break
            elif v >= k: z <<= 1
        dp[pos] = max(dp[pos], z+dp[i+1])
print(dp[0])