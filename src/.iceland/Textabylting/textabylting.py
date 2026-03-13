m=[input()for _ in range(int(input()))];k=max(map(len,m));z=[[' ']*len(m)for _ in range(k)]
for i in range(len(m)):
 for j in range(len(m[i])):z[j][i]=m[i][j]
for r in z:print(''.join(r))