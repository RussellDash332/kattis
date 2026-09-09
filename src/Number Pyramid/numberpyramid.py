N = int(input())
P = [[*map(int, input().split())] for _ in range(N)]
z = 1
while z:
    z = 0
    for r in range(N):
        for c in range(r+1):
            if P[r][c] == 100:
                if r<N-1 and P[r+1][c]<100>P[r+1][c+1]:
                    if abs(P[r+1][c]+P[r+1][c+1])>99: print('no solution'); exit()
                    P[r][c] = P[r+1][c]+P[r+1][c+1]; z = 1
                if r and c<r and P[r-1][c]<100>P[r][c+1]:
                    if abs(P[r-1][c]-P[r][c+1])>99: print('no solution'); exit()
                    P[r][c] = P[r-1][c]-P[r][c+1]; z = 1
                if r and c and P[r-1][c-1]<100>P[r][c-1]:
                    if abs(P[r-1][c-1]-P[r][c-1])>99: print('no solution'); exit()
                    P[r][c] = P[r-1][c-1]-P[r][c-1]; z = 1
            elif r<N-1 and P[r+1][c]<100>P[r+1][c+1] and P[r+1][c]+P[r+1][c+1]!=P[r][c]: print('no solution'); exit()
for r in range(N):
    for c in range(r+1):
        if P[r][c] == 100: print('ambiguous'); exit()
print('solvable')
for p in P: print(*p)