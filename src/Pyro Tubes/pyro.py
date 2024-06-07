from array import *; import sys
p = []; v = array('b', [0]*(1<<18)); c = array('i', [1<<i for i in range(18)])
while (n:=int(sys.stdin.readline())) != -1: v[n] = 1; p.append(n)
for i in p:
    m = 0
    for j in range(18):
        m += v[t:=(i^c[j])] and t > i
        for k in range(j+1, 18): m += v[t:=(i^c[j]^c[k])] and t > i
    sys.stdout.write(f'{i}:{m}\n')