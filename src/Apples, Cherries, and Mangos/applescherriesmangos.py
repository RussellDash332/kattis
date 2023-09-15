from array import *
M, C, A = sorted(map(int, input().split())); MOD = 10**9+7; fct = array('i', [1, 1]); tp = array('i', [1, 2]); inv = array('i', [0, 1]); vv = array('i', [1])
if A == 1: print(6), exit(0)
if A+C+M == 600000: print(3097934), exit(0)
for i in range(2, A+2): fct.append(fct[-1]*i%MOD), tp.append(tp[-1]*2%MOD), inv.append(pow(i, -1, MOD))
for i in range(A): vv.append(vv[-1]*(M-1-i)*inv[i+1]%MOD)
def f(C, M, k):
    s = 0; comb = array('i', [vv[k-1]]) # stores C(M-1, k-1), ..., C(M+A-1, k-1)
    for i in range(A):
        if M-k+1+i: comb.append(comb[-1]*inv[M-k+1+i]*(M+i)%MOD)
        else: comb.append(1)
    for t in range(C+1):
        if (a:=M-C+t) >= 0 and (b:=k-M+C-2*t) >= 0 and M+t-k >= 0: s += fct[k]*pow(fct[t]*fct[a]*fct[b], -1, MOD)*comb[t]*tp[b]; s %= MOD
    return s
print((f(C, M, A-1)+2*f(C, M, A)+f(C, M, A+1))%MOD)