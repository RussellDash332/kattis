N,K,*A=map(int,open(0).read().split());C=[0]*N;L=[]
for i in A:
 if C[i:=i-1]<1:
  p=[]
  while 1-C[i]:C[i]=1;p+=[i:=A[i]-1]
  L+=[len(p)]
if K in L:print(0);exit()
L.sort();S=Z=0
if L[-1]>K:print(1);exit()
while S<K:S+=L.pop();Z+=1
print(Z-1)