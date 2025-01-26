M = 101; H = 1002; D = [[0]*H for _ in range(M)]; P = 10**9+7
for i in range(M): D[i][0] = 1
for i in range(H): D[0][i] = 1
for m in range(1, M):
    for h in range(1, H):
        for i in range(max(0, h-1-m), h-1): D[m][h] += 2*D[m][i]*D[m][h-1]
        D[m][h] += D[m][h-1]**2; D[m][h] %= P
for _ in range(int(input())): m, h = map(int, input().split()); print(D[m][h+1])