import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n, m = map(int, input().split())
A = []; B = []; sa = sb = 0
for _ in range(n-1): p, a = map(int, input().split()); A.append((p, sa, sa:=a))
A.append((int(input()), sa, 10**18))
for _ in range(m-1): p, b = map(int, input().split()); B.append((p, sb, sb:=b))
B.append((int(input()), sb, 10**18))
pa = pb = ta = tb = 0
while pa < n and pb < m:
    xa = A[pa][0]; xb = B[pb][0]
    l = max(la:=A[pa][1], lb:=B[pb][1]); r = min(A[pa][2], B[pb][2])
    x = ta-tb+lb*xb-la*xa
    if xb>xa: (xb-xa)*l<=x<(xb-xa)*r!=print(x/(xb-xa))
    else: (xb-xa)*l>=x>(xb-xa)*r!=print(x/(xb-xa))
    if A[pa][2] < B[pb][2]: ta += (A[pa][2]-la)*xa; pa += 1
    else: tb += (B[pb][2]-lb)*xb; pb += 1