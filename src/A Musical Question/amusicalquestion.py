import sys; input = sys.stdin.readline; from array import *
c, _ = map(int, input().split()); c += 1; d = array('b', [0]*c*c); d[0] = 1
for i in map(int, input().split()):
    e = array('b', d)
    for j in range(c-i):
        for k in range(c): e[(j+i)*c+k] |= d[j*c+k]; e[k*c+j+i] |= d[k*c+j]
    d = e
c -= 1
for i in range(2*c, -1, -1):
    for j in range(i%2, c-abs(i-c)+1, 2):
        if d[(i+j)*c//2+i]: print((i+j)//2, (i-j)//2), exit(0)