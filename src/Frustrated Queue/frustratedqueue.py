import sys; input = sys.stdin.readline; M = 10**6; from array import *
while (s:=array('b', map(ord, input().strip()))):
    N = len(s); U = N//2+1; D = array('i', [0]*(N+1)*U); p = N*U
    for i in range(-U, 0): D[i] = 1
    for i in range(N-1, -1, -1):
        for n in range(U-1, -1, -1):
            p -= 1
            if s[i] != 40 and i+1 <= 2*n: D[p] += D[p+U]
            if s[i] != 41 and i <= 2*n+1 < n+U: D[p] += D[p+U+1]
            D[p] %= M
    print(D[0])