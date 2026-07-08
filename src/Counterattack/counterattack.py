import sys; input = sys.stdin.readline
Hj, Hr, M, N = map(int, input().split())
B = sorted(map(int, input().split()))            # Joshua
A = sorted(map(int, input().split()), reverse=1) # Rasmus
K = A.count(0)
Q = [s:=0]+[s:=s+i for i in B]
P = [s:=0]+[s:=s+i for i in A[:N-K]]
for i in range(min(len(P), len(Q))): # how many blockers?
    if P[-1]-P[i] < Hj and Q[i+max(0,M-i-K)]-Q[i] >= Hr+P[-1]-P[i]: print('YES'); exit(0)
print('NO')