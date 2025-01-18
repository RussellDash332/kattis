import sys; input = sys.stdin.readline
from bisect import *; from array import *
N = int(input())
A = array('i', map(int, input().split()))
B = array('i', map(int, input().split()))
T = array('i', [bisect_left(B, A[i]+1)-1-i for i in range(N)])
L = array('i', [10**9]); H = array('i', [10**9]); Z = 0
for i in range(N): L.append(min(L[-1], T[i])); H.append(min(H[-1], T[~i]))
for i in range(N): Z += L[i]>=-i+N<=H[~i]+N
print(Z)