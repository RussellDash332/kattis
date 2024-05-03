import sys; input = sys.stdin.readline; from array import *
n, l, h = map(int, input().split()); s = array('i', [int(input()) for _ in range(n)]); p = array('i', [x:=0]+[x:=x+i for i in s]); mi = 10**18; ma = -10**18
for k in range(l, h+1):
    for u in range(k):
        x = u; z = 0
        if x: z += p[x] > 0
        while x <= n: z += p[min(x+k, n)]-p[x] > 0; x += k
        if z < mi: mi = z
        if z > ma: ma = z
print(mi, ma)