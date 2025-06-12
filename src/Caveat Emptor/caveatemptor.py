from array import *; L, R = input().split(); M = 10**9+7; p7 = array('i', [1]); p2 = array('i', [1]); ff = array('i', [1]); rf = array('i', [1])
for i in range(200_000): p7.append(p7[-1]*7%M); p2.append(p2[-1]*2%M); ff.append(ff[-1]*(i+1)%M); rf.append(pow(ff[-1], -1, M))
def f(x):
    D = len(x); Z = 0; C = array('i', [0]); dp = array('i', [0]*(D+1))
    for d in range(2, D, 2): Z += ff[d-1]*rf[d//2-1]*rf[d//2]*p7[d//2-1]*p2[d//2]*13; Z %= M
    for i in x: C.append(C[-1]+(i=='6' or i=='8'))
    if D%2 == 0:
        for i in range(D, -1, -1):
            if C[i] > D//2: continue
            if i == D: dp[i] = D==2*C[i]; continue
            g = int(x[i])
            for v in range(int(i==0), g+1):
                if v == 4: continue
                b = C[i]+(v==6 or v==8)
                if v < int(g): dp[i] += (D>=D//2+b>=i+1)*ff[D-i-1]*rf[D//2-b]*rf[D//2-i-1+b]*p7[D//2-i-1+b]*p2[D//2-b]%M
                else: dp[i] += dp[i+1]
                dp[i] %= M
        Z += dp[0]
    return Z
print((f(R)-f(L)+('4' not in L and 2*(L.count('6')+L.count('8'))==len(L)))%M)