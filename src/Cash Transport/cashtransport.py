I=lambda:[*map(int,input().split())];N,M,K=I();A=I();E=[];Z=[];V=[0]*N
for _ in'.'*M:a,b=I();E+=[(a,b,A[a])];A[b]+=A[a];A[a]=0
for a,b,l in E[::-1]:V[a]=1;Z+=[l]*(V[b]<1)
print(sum(sorted(Z)[-K:]))