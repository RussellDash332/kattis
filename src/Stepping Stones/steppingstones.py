N,M,*H=map(int,open(0).read().split());Q=[*range(M)];D=[1]*M+[1e9]*-~(M*~-N);H+=0,
for u in Q:
 for v,w in((h:=H[u],0),(-h,0),(0,h),(0,-h)):
  if(y:=u//M+v)>-1<(c:=u%M+w)<M and D[z:=min(y*M+c,N*M)]>D[u]+1:D[z]=D[u]+1;Q+=[z]
print([-1,Z:=D[-1]][Z<1e8])