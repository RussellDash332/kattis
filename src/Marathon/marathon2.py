from collections import *; import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
def turn(j, k):
    l = 1; r = N+1
    while l < r:
        if f(m:=(l+r)//2,k) <= f(m,j): r = m
        else: l = m+1
    return l
def f(i, j): u = min(d:=P[i]-P[j], X); return dp[j] + u*S + (d-u)*H + Y*H*S
N, X, Y = map(int, input().split()); H, S = map(int, input().split()); P = [1]+[0]*42194
for _ in range(N):
    x = int(input())
    if x < 42195: P[x] = 1
P = [i for i in range(42195) if P[i]]; N = len(P); P.append(42195); dp = [0]*(N+1); Q = deque([0])
for i in range(1, N+1):
    while len(Q) > 1 and turn(Q[0], Q[1]) <= i: Q.popleft()
    dp[i] = f(i, Q[0])
    if i == N: break
    while len(Q) > 1 and turn(Q[-2], Q[-1]) >= turn(Q[-1], i): Q.pop()
    Q.append(i)
Z = int(dp[-1]/H/S-Y); print(f'{str(Z//3600).zfill(2)}:{str(Z//60%60).zfill(2)}:{str(Z%60).zfill(2)}')