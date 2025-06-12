import sys; input = sys.stdin.readline
n, m = map(int, input().split()); Z = [0]*n; M = [*Z]; N = 1500
for _ in range(m):
    a, b = map(int, input().split()); a -= 1; b -= 1
    if M[a] == 0: Z[a] = N
    if M[b] == 0: Z[b] = N
    x, y = Z[a], Z[b]; Z[a] += min(max(0, (3*y-x)//2)*(M[b]+1)//(M[a]+M[b]+2), 1000); Z[b] -= min(max(0, y-int(x/6+y/2))*(M[a]+1)//(M[a]+M[b]+2), 1000)
    if M[a] == 0 and M[b]: N = Z[a]
    if M[b] == 0 and M[a]: N = Z[b]
    M[a] += 1; M[b] += 1; print(Z[a], Z[b])