R, C = map(int, input().split())
H = {}
for i in range(R):
    S = input()
    for j in range(C): H.setdefault(S[2*j], []).append((i, j))
for v in H.values():
    if (max(r for r,c in v)-min(r for r,c in v)+1)*(max(c for r,c in v)-min(c for r,c in v)+1) != len(v): print('NO'); exit()
print('YES')