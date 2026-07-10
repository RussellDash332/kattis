N,*A=map(int,open(0).read().split());L=[0];R=[];Z=0
for i in range(N):(R,L)[i%2].append(Z:=A[i]-Z)
R=min(R or[0]);L=min(L);print(max(R+L+1,0)*(R>=0))