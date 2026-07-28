N,A,B=map(int,input().split());M=10301;Z=[]
for K in(A,B):
 D=[0]*-~N;E=[*D];D[K]=E[0]=1
 for l in range(K,N+1):
  for s in range(N+1):E[s]=(E[s]+E[s-l])%M
  for t in range(N+1):D[t]=(D[t]+E[t-2*l])%M
 Z+=[D]
P,Q=Z;p=0;R=[p:=p+i for i in Q]
print(sum(P[i]*R[N-i]for i in range(N+1))%M)