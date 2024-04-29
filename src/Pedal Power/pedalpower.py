import sys; input = sys.stdin.readline
V = int(input()); I = float('inf'); b = [[I]*V for _ in range(V)]; nb = [[I]*V for _ in range(V)]
for i in range(V): b[i][i] = nb[i][i] = 0
for _ in range(int(input())): x, y, w = map(int, input().split()); b[x][y] = b[y][x] = w
for k in range(V):
    for i in range(V):
        for j in range(V): b[i][j] = min(b[i][j], b[i][k]+b[k][j])
for _ in range(int(input())): x, y, w = map(int, input().split()); nb[x][y] = nb[y][x] = w
for k in range(V):
    for i in range(V):
        for j in range(V): nb[i][j] = min(nb[i][j], nb[i][k]+nb[k][j])
q = int(input()); a = [0, *map(int, input().split()), 0]; dp = [I]*V; dp[0] = 0
for i in range(q+1):
    ss, ee = a[i], a[i+1]; tmp = [I]*V
    for j in range(V):
        # bike currently at j, want to go from ss to ee
        for k in range(V):
            # move bike from j to k?
            if j == k: tmp[k] = min(tmp[k], dp[j]+nb[ss][ee]) # no need to move bike
            else: tmp[k] = min(tmp[k], dp[j]+nb[ss][j]+b[j][k]+nb[k][ee]) # go to j, move bike to k, go to ee
    dp = tmp
print(dp[0])