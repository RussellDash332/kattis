Q=lambda i,j:int(input(f'? {i} {j}\n'));S=[1];R=range
for i in R(1,int(input())):
 if Q(i,i+1):S[-1]+=1
 else:S+=1,
p=S[0]+1;u,v=T=[0,1]
for s in S[1:-1]:u,v=v,[3-u-v,u][Q(p-1,p:=p+s)];T+=v,
M=len(A:=[3]+[x for i,j in zip(T,S)for x in(4,i)*j]+[4,5]);print('!',max(next(p for p in R(M)if A[~p+i]-A[i-~p])for i in R(1,M-1)))