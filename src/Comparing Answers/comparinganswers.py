import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
A = [0]*10**6
while (n:=int(input())):
    D = [0]*n; E = [0]*n; ok = 1; r = 0
    for i in range(n):
        p = 0
        for j in map(int, input().split()): A[n*i+p] = j; p += 1; D[i] += j*p
    for i in range(n):
        for j in range(n): E[i] -= A[r]*D[j]; r += 1
        p = 1
        for j in map(int, input().split()): E[i] += j*p; p += 1
        if E[i]:
            ok = 0
            for _ in range(n-1-i): input()
            break
    print('YNEOS'[1-ok::2]); input()