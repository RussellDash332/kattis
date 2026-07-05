N=int(input());S=input();Z=0;C=[0]+[i for i in range(1,N)if S[i-1]<'b'>S[i]]+[N]
for s,t in zip(C,C[1:]):
 A=[len(i)+1for i in S[s:t].split('a')];P=[p:=0]+[p:=p+i for i in A];K=len(A);T=sum((K-1-i)*A[i]for i in range(K-1))
 for i in range(K-1,0,-1):Z+=T*A[i];T-=P[i]
print(Z)