def kmp(T, P):
    n, m = len(T), len(P); b = [0]*(m+1); i, j = 0, -1; b[0] = -1
    while i < m:
        while j >= 0 and P[i] != P[j]: j = b[j]
        i += 1; j += 1; b[i] = j
    i = j = 0; z = [0]*n
    while i < n:
        while j >= 0 and T[i] != P[j]: j = b[j]
        i += 1; j += 1
        if j == m: z[i-m] = 1; j = b[j]
    return z
for _ in range(int(input())): s, t = input().split(); p = [u:=0]+[u:=u+i for i in kmp(s, t)]; k = len(s)-len(t); print(['Bob', 'Alice'][all(p[i+k//2+1]-p[i]>0 for i in range(k//2+k%2+1))])