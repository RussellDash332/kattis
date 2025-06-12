import sys; input = sys.stdin.readline; TC = 0

def d2(a, b):
    return (a[0]-b[0])**2+(a[1]-b[1])**2

def pip(p):
    z = False
    for i in range(n):
        a = (P[i][0]-p[0], P[i][1]-p[1]); b = (P[(i+1)%n][0]-p[0], P[(i+1)%n][1]-p[1])
        if a[1] > b[1]: a, b = b, a
        if a[1] <= 0 and b[1] > 0 and a[0]*b[1] < a[1]*b[0]: z = not z
        if a[0]*b[1] == a[1]*b[0] and a[0]*b[0]+a[1]*b[1] <= 0: return True
    return z

while (n:=int(input())):
    TC += 1; P = [[*map(int, input().split())] for _ in range(n)]; P.append(P[0]); Q = int(input()); print('Case', TC)
    for _ in range(Q):
        x, y = map(int, input().split()); hit = pip(p:=(x, y)); best = 1e18
        for i in range(n):
            x1, y1 = P[i]; x2, y2 = P[i+1]; A = y2-y1; B = x1-x2; r = (y-y1)*A-(x-x1)*B; d = A*A+B*B
            if r < 0: best = min(best, d2(p, P[i]))
            elif r > d: best = min(best, d2(p, P[i+1]))
            else: best = min(best, (A*(x-x1)+B*(y-y1))**2/d)
        if best == 0: print('Winged!')
        elif hit: print('Hit!', best**.5)
        else: print('Miss!', best**.5)