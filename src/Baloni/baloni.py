import sys; input(); from array import *
b = array('i', [0]*(10**6+1)); r = 0
for i in [*map(int, sys.stdin.readline().split())]:
    b[i-1] += 1
    if b[i]: b[i] -= 1
    else: r += 1
print(r)