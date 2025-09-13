N,T,*A=map(int,open(0).read().split());t=1
while 1:
 V=[sum(A[t*i:t*i+t])//t for i in range(N//t)]
 if max([abs(a-b)for a,b in zip(V,V[1:])]or[0])<=T:print(t);break
 t+=1