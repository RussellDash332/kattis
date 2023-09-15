import sys; input = sys.stdin.readline
from array import *
def can(x):
    bm = 0
    for offset in range(n):
        if a[offset] & bm == a[offset]: continue
        bm |= a[offset]; sec = 0; b = 0
        for pos in range(offset+1, offset+1+n):
            b |= a[pos%n]
            if x & b == x: b = 0; sec += 1
            if sec >= k: return 1
n, k = map(int, input().split()); a = array('i', [*map(int, input().split())]); ans = 0
for i in range(30, -1, -1):
    if can(ans|(b:=1<<i)): ans |= b
print(ans)