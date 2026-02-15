from math import *
def area(p, q, r):
    return ((q[0]-p[0])*(r[1]-p[1])-(r[0]-p[0])*(q[1]-p[1]))/2
N = int(input())
P = sorted(([*map(int, input().split())] for _ in range(N-1)), key=lambda x: atan2(x[1], x[0]))
*h, H = sorted(int(input()) for _ in range(N)); A = []
for i in range(N-1): A.append(area(P[i], (0, 0), P[i-1]))
print(sum(x*y for x,y in zip(sorted(A[x]+A[x-1] for x in range(N-1)), h))/3+sum(A)*H/3)