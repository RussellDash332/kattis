n, a2, a3, m21, m31, c2, c3 = map(int, open(0).read().split()); a0 = 100-a2-a3
dp = [0]*10201
for _ in range(n):
    dq = [0]*10201
    for m2 in range(101):
        for m3 in range(101): dq[m2*101+m3] = (a2*(m2*(dp[min(m2+c2, 100)*101+m3]+2)+(100-m2)*dp[max(m2-c2, 0)*101+m3])+a3*(m3*(dp[m2*101+min(m3+c3, 100)]+3)+(100-m3)*dp[m2*101+max(m3-c3, 0)])+a0*100*dp[m2*101+m3])/10000
    dp = dq
print(dp[m21*101+m31])