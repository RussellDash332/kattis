I=lambda:input().split();t,p=map(int,I());S=[*map(float,I())];P=[*map(float,I())];T=[I()for _ in'.'*~-t];X=I().count('X')+2;Z=1
for k in range(t-1):
 z=T[k];D=[0]*-~p*X;D[0]=1
 for i in range(p):
  for j in range(X-1):
   v=D[u:=i*X+j];y=S[k]*P[i]
   if z[i]<'?':D[u+X]=v
   elif z[i]<'X':D[u+X+1]+=y*v;D[u+X]+=(1-y)*v
   else:D[u+X+1]=v
 Z*=sum(D[-X:-1])
print(Z)