import sys; input = sys.stdin.readline
N, Q = map(int, input().split())
G = [[] for _ in range(N)]; F = [[0]*51 for _ in range(N)]; R = [0]*N; T = [N]+[0]*50
for _ in range(Q):
    c, *v = input().split()
    if c == 'F': a, b = map(int, v); a -= 1; b -= 1; G[a] += [b]; G[b] += [a]; F[a][R[b]] += 1; F[b][R[a]] += 1
    elif c == 'A':
        x = int(v[0])-1; T[R[x]] -= 1
        for y in G[x]: F[y][R[x]] -= 1
        R[x] += 1; T[R[x]] += 1
        for y in G[x]: F[y][R[x]] += 1
    else: # Q
        x = int(v[0])-1; z = 50
        while ~z:
            if T[z] != F[x][z]+(R[x]==z): break
            z -= 1
        print(z)