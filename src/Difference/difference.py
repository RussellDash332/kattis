from array import *
r, m = map(int, input().split()); A = array('i', [r]); U = array('b', [0]*(r+1)); U[0] = U[r] = n = 1
while True:
    if len(U) > m and U[m]: print(n); break
    while U[r-A[-1]]: U.append(0); r += 1
    for i in A: U[r-i] = 1
    A.append(r); U[r] = 1; n += 1