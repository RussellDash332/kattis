N=int(input());M=[input()for _ in'.'*N];S={(i,j)for i in range(N)for j in range(N)}
for L in range(3,N,2):
 for i in range(N-L):
  for j in range(N-L+1):
   T={(i,k)for k in range(j,j+L)}|{(k,j+L//2)for k in range(i,i+L+1)}
   if all(M[r][c]<'.'for r,c in T)and all(M[r][c]>'*'for r,c in S-T):print('Y')<exit()
print('N')