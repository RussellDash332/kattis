import sys; input = sys.stdin.readline
def bt(n, d, s, a, p, m):
    if d not in m or m[d] < s: m[d] = s
    if n >= 0: bt(n-1, d+a[n], s+a[n], a, p, m); bt(n-1, d-a[n], s+a[n], a, p, m); bt(n-1, d, s, a, p, m)
while (N:=int(input())):
    A = [int(input()) for _ in range(N)]; A1 = A[:N//2]; A2 = A[N//2:]; P1 = [s:=0, *((s:=s+i) for i in A1)]; P2 = [s:=0, *((s:=s+i) for i in A2)]; M1 = {}; M2 = {}; Z = 0; bt(len(A1)-1, 0, 0, A1, P1, M1); bt(len(A2)-1, 0, 0, A2, P2, M2)
    for i in M1:
        if -i in M2 and Z < M1[i]+M2[-i]: Z = M1[i]+M2[-i]
    print(P1[-1]+P2[-1]-Z)