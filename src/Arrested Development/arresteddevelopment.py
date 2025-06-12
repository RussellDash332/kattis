from array import*;n=int(input());A=[];B=[]
for _ in'.'*n:a,b=map(int,input().split());A.append(a);B.append(b)
if sum(A)>sum(B):A,B=B,A
H=array('I',[10**9]*(M:=sum(A)+1));H[0]=0
for a,b in zip(A,B):
 for k in range(M):H[k]+=b
 for k in range(M-1,a-1,-1):H[k]=min(H[k],H[k-a]-b)
print(min(max(k,H[k])for k in range(M)))