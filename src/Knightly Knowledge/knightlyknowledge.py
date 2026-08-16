R = {}; C = {}; S = [set(), set()]
for x, K in enumerate(map(int, input().split())):
    for _ in range(K):
        r, c = map(int, input().split()); S[x].add((r, c))
        if r not in R: R[r] = [0, 0]
        R[r][x] += 1
        if c not in C: C[c] = [0, 0]
        C[c][x] += 1
for r, c in [*S[1]]:
    if R[r][0]>1 or C[c][0]>1: R[r][1] -= 1; C[c][1] -= 1; S[1].discard((r, c))
print(*max([(r, c, (a:=R[r][0]<1)*(b:=C[c][0]<1)*((r,c) in S[1])-a*R[r][1]-b*C[c][1]-(a:=R[r][0]<2)*(b:=C[c][0]<2)*((r,c) in S[1])+a*R[r][1]+b*C[c][1]) for r in R for c in C], key=lambda x:x[2], default=(0, 0, 0)))