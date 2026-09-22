T=sorted(range(N:=len(S:=input())),key=lambda x:S[x]);V=[0]*N;A=sorted(S);Z=[]
for i in range(N):
 if V[i]<1:
  V[i]=1;C=[i]
  while V[u:=T[C[-1]]]<1:V[u]=1;C+=[u]
  while len(C)>1:
   if A[a:=C.pop()]<A[b:=C[-1]]:a,b=b,a
   A[a],A[b]=A[b],A[a];Z+=[(a+1,b+1)]
for i in Z:print(*i)