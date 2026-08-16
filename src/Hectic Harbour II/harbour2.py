N,*_=map(int,input().split());Z=0;A=[*map(int,input().split())]+[*map(int,input().split())][::-1];H={e:i for i,e in enumerate(A)};L=[-1]+[*range(N)];R=[*range(1,N+1)]+[-1]
for i in R[:-1]:
 t=H[i];l=L[t];r=R[t]
 if~l:R[l]=r
 if~r:L[r]=l
 Z+=(A[l]<1<l+2)|(A[r]<1<r+2)
print(Z)