N = int(input()); B = [int(input()) for _ in range(N)]; P = sum(B)//3
if N == 3: print(1, 1, P-2), exit(0)
if N == 4: print(*(P-B[(i+2)%N] for i in range(4))), exit(0)
A = [B[(i+2)%N]-B[(i+1)%N] for i in range(N)]; S = [None]*N
if N % 3:
    S[p:=0] = 1
    while S[(p+3)%N] == None: S[(p+3)%N] = A[p]+S[p]; p = (p+3)%N
    M = (P-sum(S))//N
    for i in range(N): S[i] += M
    print(*S)
else:
    for i in range(2):
        S[i] = 1
        for j in range(i+3, N, 3): S[j] = A[j-3]+S[j-3]
        M = min(S[i::3])-1
        for j in range(i, N, 3): S[j] -= M
    S[2] = B[1]-S[0]-S[1]
    for j in range(5, N, 3): S[j] = A[j-3]+S[j-3]
    print(*S)