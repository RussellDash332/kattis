def pip(p, P):
    z = False; n = len(P)
    for i in range(n):
        a = (P[i][0]-p[0], P[i][1]-p[1]); b = (P[(i+1)%n][0]-p[0], P[(i+1)%n][1]-p[1])
        if a[1] > b[1]: a, b = b, a
        if a[1] <= 0 and b[1] > 0 and a[0]*b[1] < a[1]*b[0]: z = not z
        if a[0]*b[1] == a[1]*b[0] and a[0]*b[0]+a[1]*b[1] <= 0: return 'on'
    return 'oiunt'[z::2]
while True:
    n = int(input())
    if n == 0: break
    pts = [list(map(int, input().split())) for _ in range(n)]
    for _ in range(int(input())): print(pip(list(map(int, input().split())), pts))