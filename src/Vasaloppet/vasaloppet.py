import sys; input = sys.stdin.readline; from array import *; from collections import *
N, T, S = map(int, input().split()); A = deque(); L = array('i'); M = C = 0; W = deque()
for _ in range(N): l, r = map(int, input().split()); A.append((l, r)); L.append(l)
for i in L:
    while W and W[0][0] < i: l, r = W.popleft(); C -= r-l
    while A:
        if i+S <= A[0][0]: break
        if i >= A[0][1]: A.popleft()
        elif i+S < A[0][1]: l, r = A.popleft(); W.append((l, i+S)); A.appendleft((i+S, r)); C += i+S-l
        else: W.append(A.popleft()); C += W[-1][1]-W[-1][0]
    if M < C: M = C
print(S-M)