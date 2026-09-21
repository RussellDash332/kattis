N=int(input());S=input();T=450;D=[0]*-~N*T
for i in range(N,-1,-1):
 for j in range(T-2,1,-1):
  u=i*T+j
  if i==N:D[u]=1
  elif S[i]>'#':D[u]=(D[u+T]+D[min(i+j,N)*T+j+1])%(10**9+7)
print(D[2])