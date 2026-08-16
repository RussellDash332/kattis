t=input()
while 1:
 S=t;N=len(t)
 if S=='*':break
 C=[[]for _ in'.'*N]
 while 1:
  t=input()
  if t[0]in'*<=>':break
  for i,e in enumerate(t.split('&')):C[i]+=[e]
 M=[max(len(c)for c in k)for k in C];P=sum(m+2for m in M)+N+1;Z=[[' ']*P for _ in range(len(C[0])+3)];Z[0][0]=Z[0][-1]=Z[-1][0]=Z[-1][-1]='@';q=0
 for i in range(1,P-1):Z[0][i]=Z[-1][i]=Z[2][i]='-'
 for i in range(1,len(C[0])+2):
  Z[i][0]='|';p=0
  for j in M:Z[i][p:=p+j+3]='|+'[i==2]
  Z[2][-1]='|'
 for i in range(len(C)):
  m=M[i];h,*c=C[i];b=[0,(z:=m-len(h))//2,z][a:=ord(S[i])%3]
  for j in range(len(h)):Z[1][q+2+j+b]=h[j]
  for j,u in enumerate(c):
   b=[0,(z:=m-len(u))//2,z][a]
   for k in range(len(u)):Z[3+j][q+2+k+b]=u[k]
  q+=m+3
 print('\n'.join(map(''.join,Z)))