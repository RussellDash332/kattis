N=int(input());F=[K:=0]*-~N;W=[*F];Q=[];Z=[]
for i in range(N):c,x=map(int,input().split());Q+=[(c,x)];K+=c&1;F[i]=i&-i
M=K
for c,x in Q[::-1]:
 k=0
 for i in range(20):
  if(t:=k|(1<<(19-i)))<=M and F[t]<x:x-=F[k:=t]
 if c&1:
  W[k]=K;K-=1;k+=1
  while k<=M:F[k]-=1;k+=k&-k
 else:Z+=[k]
for k in Z[::-1]:print(W[k])