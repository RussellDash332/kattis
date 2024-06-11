import sys; input = sys.stdin.readline
n, m = map(int, input().split()); c = [*map(int, input().split())]; h = [-1]*n*n*2; F = [m]
for _ in range(n): F.append(int(2*F[-1]/3))
def dp(t, s, r):
    if t == n: return 0
    if h[(k:=2*n*t+2*s+r)] != -1: return h[k]
    h[k] = max(min(c[t], F[s])+dp(t+1, s+1, 0), dp(t+1, (max(s-1, 0), 0)[r], 1)); return h[k]
print(dp(0, 0, 0))