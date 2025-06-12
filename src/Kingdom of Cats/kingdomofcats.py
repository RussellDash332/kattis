def cross(a, b, c): return (b[0]-a[0])*(c[1]-a[1])-(c[0]-a[0])*(b[1]-a[1])
def check(a, b, c, d):
    for a, b, c, d in ((a, b, c, d), (a, c, b, d), (a, b, d, c)):
        if max(v:=(cross(a, b, c), cross(b, c, d), cross(c, d, a), cross(d, a, b)))*min(v) > 0: return 1
    return 0
while (n:=int(input())): P = [[*map(int, input().split())] for _ in range(n)]; print(sum(check(P[i], P[j], P[k], P[l]) for i in range(n) for j in range(i) for k in range(j) for l in range(k)))