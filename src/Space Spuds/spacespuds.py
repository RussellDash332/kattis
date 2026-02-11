from math import *
N = int(input())
P = [[*map(int, input().split())] for _ in range(N)]
A = B = 0
for i in range(N):
    x1, y1 = P[i]; x2, y2 = P[i-1]
    A += x1*y2-x2*y1; B += gcd(x1-x2, y1-y2)
print((abs(A)-B)//2+1)