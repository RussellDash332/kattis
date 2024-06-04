import sys; input = sys.stdin.readline; from array import *
n = int(input()); a = array('i', map(int, input().split())); r = 0; m = max(a)*n; b = array('i'); v = array('i'); i = 0
while i < n:
    if a[i] > 1: b.append(a[i]); v.append(a[i]); i += 1
    else:
        c = 0
        while i < n and a[i] == 1: c += 1; i += 1
        b.append(c); v.append(1)

def sol(k, ux, uy): # surprisingly fast enough
    w = 0
    for x in range(ux+1): w += 0 <= k-x <= uy
    return w

for i in range(len(b)):
    ss = (1, b[i])[v[i]>1]; se = b[i]; t = v[i]
    for j in range(i+1, len(b)):
        if v[j] > 1:
            ss += b[j]; se += b[j]; t *= v[j]
            if t > m: break
            r += ss <= t <= se
        else:
            if v[i] > 1: r += ss+1 <= t <= se+b[j]
            elif t-se+b[i] <= b[i]+b[j]: r += sol(t-se+b[i]-2, b[i]-1, b[j]-1)
            ss += b[j]; se += b[j]
print(r)