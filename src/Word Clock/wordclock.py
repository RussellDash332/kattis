r,c,n=map(int,input().split());W=input().split();h={1<<i:i for i in range(18)};P=[-~n*[0]for _ in'.'*n];D=[-~n*[0]for b in range(1<<n)]
if max(map(len,W))>c:print('impossible');exit()
for i in range(n):
 for j in range(n):
  for k in range(1,min(len(W[i]),len(W[j]))+1):
   if W[i][-k:]==W[j][:k]:P[i][j]=k
for b in range(1,1<<n):
 for i in range(-1,n):
  d=b;z=2*r*c
  while d:
   j=h[u:=d&-d];d^=u;v=D[b^u][i]
   if~i and W[j]in W[i]:z=min(z,v)
   else:
    k=len(W[j]);p=k-P[j][i];v=D[b^u][j]
    if v%c+k>c:z=min(z,c-v%c+k+v)
    else:z=min(z,p+v)
  D[b][i]=z
Z=D[B:=2**n-1][i:=-1];M=['X'*c]*r
if Z>r*c:print('impossible');exit()
while B:
 d=B
 while d:
  j=h[u:=d&-d];d^=u;v=D[B^u][i]
  if~i and W[j]in W[i]:
   if v==Z:B^=u;break
  else:
   v=D[B^u][j];k=len(W[j]);p=k-P[j][i]
   if v%c+k>c:
    if c-v%c+k+v==Z:s=Z-k;B^=u;Z=v;i=j;t=M[s//c];M[s//c]=t[:s%c]+W[j]+t[s%c+k:];break
   elif p+v==Z:s=Z-p;B^=u;Z=v;i=j;t=M[s//c];M[s//c]=t[:s%c]+W[j]+t[s%c+k:];break
print(*M,sep='\n')