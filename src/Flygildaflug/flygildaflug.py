Q = int(input())
m1, m2, m3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())
M = 10**9+7; D = [[0]*1002 for _ in range(1002)]; D[0][0] = 1
for x in range(1001):
    for y in range(1001): D[x+1][y] = (D[x][y-1]*(m1*(y-1)+b1)*(y>0)+D[x][y]*(m2*y+b2)+D[x][y+1]*(m3*(y+1)+b3))%M
for _ in range(Q): print(D[int(input())][0])