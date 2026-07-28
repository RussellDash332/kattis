R,C=map(int,input().split());N=len(S:=input());P={(0,0)};r=c=0
for i in range(N):d=S[i]<'Q';P.add((r:=r+d,c:=c+1-d))
A=[0];B=[0];X=[0];Y=[0]
for r,c in sorted(P):
 for i,j,Z in((0,1,A),(-1,0,B),(1,0,X),(0,-1,Y)):Z+=[Z[-1]+((r+i,c+j)not in P)*(R>r+i>-1<c+j<C)]
N+=1;print(min(A[i-1]-B[i+1]for i in range(1,N))+min(X[i-1]-Y[i+1]for i in range(1,N))+B[N]+Y[N])