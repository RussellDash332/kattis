from array import *
m, k = map(int, input().split()); L = k+1; M = array('i', [1]*L)
for i in range(2, int(L**.5)+1):
    if M[i] == 1:
        for j in range(i, L, i): M[j] *= -i
        for j in range(i*i, L, i*i): M[j] = 0
for i in range(2, L):
    if M[i] == i: M[i] = 1
    elif M[i] == -i: M[i] = -1
    elif M[i] < 0: M[i] = 1
    elif M[i] > 0: M[i] = -1
MOD = 998244353; print((sum(M[i]*(pow(k//i*2+1, m, MOD)-1) for i in range(1, k+1))+1)%MOD)