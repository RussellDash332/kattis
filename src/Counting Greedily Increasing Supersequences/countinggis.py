import sys; input = sys.stdin.readline; from array import *
N, L = map(int, input().split()); A = array('i', map(int, input().split())); Z = array('i'); C = K = 0; X = 1; M = 10**9+7
if A[-1] != N or any(A[i]>=A[i+1] for i in range(L-1)): print(0), exit(0)
for i in range(L):
    while C <= A[i]-1: Z.append(L-i); C += 1
while C < N: Z.append(L-i); C += 1
for i in range(N)[::-1]:
    if A and A[-1] == i+1: A.pop()
    else: X *= Z[i]+K; K += 1; X %= M
print(X)