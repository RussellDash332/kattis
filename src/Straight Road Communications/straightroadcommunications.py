N,I,B=map(int,input().split());K=[];C=M=0
for _ in'.'*N:a,b=map(int,input().split());K.extend(((2*min(a,b)-B-1,1),(2*max(a,b)+B+1,-1)))
for _,v in sorted(K):M=max(M,C:=C+v)
print('im'*(M>I)+'possible')