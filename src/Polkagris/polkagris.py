from array import *
n, m = map(int, input().split()); S = '$'+input()+'^'; T = input(); p = array('i', [0]*(n+2)); l = r = 1
for i in range(1, n+1):
    p[i] = max(0, min(r-i, p[l+r-i]))
    while S[i-p[i]] == S[i+p[i]]: p[i] += 1
    if i+p[i] > r: l = i-p[i]; r = i+p[i]
S, p = S[1:-1], p[1:-1]; b = array('i', [0]*(m+1)); i, j = 0, -1; b[0] = -1
while i < m:
    while j >= 0 and T[i] != T[j]: j = b[j]
    i += 1; j += 1; b[i] = j
def f(T):
    i = j = 0; u = []
    while i < n:
        while j >= 0 and S[i] != T[j]: j = b[j]
        i += 1; j += 1
        if j == m: u.append(i-m); j = b[j]
    L = array('i', [0]*(n+1)); R = array('i', [0]*(n+1)); L[1] = R[-2] = 1
    for i in range(1, n): L[i+1] = L[i]+(L[i]>L[i-p[i]+1]); R[~i-1] = R[~i]+(R[~i]>R[~i+p[~i]-1])
    for l in u:
        if L[l+1]-L[l] and R[l+m-1]-R[l+m]: print('possible'), exit()
f(T); f(T[::-1]); print('impossible')