I=input
for _ in'.'*int(I()):
 n=int(I());P=[*map(int,I().split())];R=[0]*n;C=[0]*n
 for i in range(n-1):
  if P[i+1]>P[i]:d=P[i+1]-P[i];R[i]=R[i+1]=d;C[i]=P[i]//d;C[i+1]=P[i+1]//d
  else:R[i+1]=P[i+1];C[i+1]=1;R[i]=P[i+1]-1;C[i]=P[i]//R[i]
 print(max(R+C))