import sys; input = sys.stdin.readline
X, Y, N = map(int, input().split()); R = {}
for _ in range(N):
    a, b = map(int, input().split())
    if a not in R: R[a] = []
    R[a].append(b)
sx = 1; mx = max(R)
for x in sorted(R):
    ex = x if x != mx else X; sy = 1; my = max(R[x])
    for y in sorted(R[x]): print(sx, sy, ex, y if y != my else Y); sy = y+1
    sx = x+1
print(0)