import sys; input = sys.stdin.readline
N, B = map(int, input().split()); A = T = 1; X = 0; Z = 10**18
for _ in range(N):
    S = E = 0; X += 1
    for _ in range(int(input())): s, e = map(int, input().split()); k = max(((S:=max(S, s-E))-A+T-1)//T, 0); A += k*T; X += k; T = max(T, E:=E+e); Z = min(Z, max((B-A-E+T-1)//T, 0)+X)
    A += E
print(Z)