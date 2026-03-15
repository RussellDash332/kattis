# if all numbers are positive
import os, sys
c = 0; W = []; F = W.append
for i in os.read(0, os.fstat(0).st_size):
    if i > 45: c = c*10+i-48
    elif c: F(c); c = 0
sys.stdout.write(f'{W[0]}\n')

# if some numbers are nonpositive
import os, sys
c = r = m = 0; W = []; F = W.append
for i in os.read(0, os.fstat(0).st_size):
    if i > 45: c = c*10+i-48; r = 1
    elif i == 45: m = 1
    elif r: F(-c if m else c); c = r = m = 0
sys.stdout.write(f'{W[0]}\n')

# otherwise
import sys; input = sys.stdin.readline
N = int(input())
S = input().strip()
sys.stdout.write(f'{N} {S}\n')