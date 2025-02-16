import sys; input = sys.stdin.readline
MOD = 10**9+7; N,M,K = map(int,input().split()); Q = []; R = {}; C = {}; a = b = 1; k = {0,1}
for _ in range(K): c,x,y = input().split(); Q.append((2*(c=='+')-1,int(x)-1,int(y)-1))
for s,x,y in Q:
    v = [s,-s][x%2]; w = [s,-s][y%2]
    if x in R and R[x] != w: a = 0
    if y in C and C[y] != v: b = 0
    R[x] = w; C[y] = v; k.discard(((s+1)//2+x+y)%2)
print((a*pow(2,N-len(R),MOD)+b*pow(2,M-len(C),MOD)-len(k))%MOD)