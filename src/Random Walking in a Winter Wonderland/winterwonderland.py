R, C = map(int, input().split())
M = ''.join(input() for _ in '.'*R)
S = int(input())+1
D = [0]*R*C*S
D[M.index('h')*S] = 1
K = ((0, 1), (1, 0), (-1, 0), (0, -1))
for i in range(S-1):
    for r in range(R):
        for c in range(C):
            if M[t:=r*C+c]>'.':
                for dr, dc in K:
                    if R>r+dr>-1<c+dc<C and M[u:=r*C+c+dr*C+dc]>'.': D[u*S+i+1] += D[t*S+i]
print(D[M.index('d')*S+S-1])