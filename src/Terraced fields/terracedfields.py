import sys; input = sys.stdin.readline
M = {}; D = 19
def dp(i=0, t=0, m=0, c=0):
    if i==D: return (m==0)*c
    K = (32*i+16*t+2*m)*D+c
    if K in M: return M[K]
    z = 0; k = n//(p:=10**(D-1-i))%10
    for d in range(10 if t else k+1): z += dp(i+1, t|(d<k), (m+d*p)%8, c+(d==6 or d==8))
    M[K] = z; return z
for _ in range(int(input())): M = {}; n = int(input()); print(dp()+(n%8 and str(n).count('6')+str(n).count('8')))