R,C=map(int,input().split());M=''.join(input()for _ in'.'*R);D=[0]*R*C;T=((-1,0),(0,1),(0,-1),(1,0));Q=[]
for u in range(R*C):r=u//C;c=u%C;b=(M[u]>'-')*any(not R>r+i>-1<c+j<C or M[u+i*C+j]<'X'for i,j in T);D[u]=b;Q+=[u]*b
for u in Q:
 r=u//C;c=u%C
 for i,j in T:
  if R>r+i>-1<c+j<C and(M[v:=u+i*C+j]>'-')*(D[v]<1):D[v]=D[u]+1;Q+=[v]
print(max(D))