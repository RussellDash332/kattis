import sys; input = sys.stdin.readline; from array import *

def ccw(p, q, r):
    return (q[0]-p[0])*(r[1]-p[1]) > (r[0]-p[0])*(q[1]-p[1])

def chull(pts):
    if len(pts) < 3: return pts
    pts, n = sorted(pts), len(pts)
    upper, lower = pts[:2], pts[-1:-3:-1]
    for i in range(2, n):
        while len(upper) > 1 and not ccw(upper[-2], upper[-1], pts[i]): upper.pop()
        upper.append(pts[i])
    for i in range(n-2, -1, -1):
        while len(lower) > 1 and not ccw(lower[-2], lower[-1], pts[i]): lower.pop()
        lower.append(pts[i])
    upper.pop(); lower.pop(); upper.extend(lower); return upper

def area(x, y):
    return abs(c+x*dy-y*dx)

for _ in range(int(input())):
    n = len(p:=chull([[*map(int, input().split())] for _ in range(int(input()))])); m = 0; X = array('i', (q[0] for q in p)); Y = array('i', (q[1] for q in p))
    for i in range(n):
        a = i; b = i+1 # rotating caliper style
        for j in range(i+1, n):
            dx = X[i]-X[j]; dy = Y[i]-Y[j]; c = X[i]*Y[j]-X[j]*Y[i]
            while a < j and area(X[a], Y[a]) < area(X[a+1], Y[a+1]): a += 1
            while b < n-1 and area(X[b], Y[b]) < area(X[b+1], Y[b+1]): b += 1
            if (M:=area(X[a], Y[a])+area(X[b], Y[b])) > m: m = M
    print(str(m//2)+'.5'*(m%2))