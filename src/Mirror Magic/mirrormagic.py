import sys; input = sys.stdin.readline
N = int(input())
A = [complex(*map(int, input().split())) for _ in range(N)]
B = [complex(*map(int, input().split())) for _ in range(N)]
cA = sum(A)/N; cB = sum(B)/N
c = (cA+cB)/2; v = cB-cA
if len({[s:=((p-c)*v.conjugate()).real, (s>0)-(s<0)][1] for p in A}) > 1 or v==0: print('impossible'); exit()
C = [c-(v/v.conjugate())*(q.conjugate()-c.conjugate()) for q in A]
for p, q in zip(sorted(B, key=lambda x:(x.real, x.imag)), sorted(C, key=lambda x:(x.real, x.imag))):
    if abs(p-q)>1e-8: print('impossible'); exit()
print('possible')