def g(n,b):
 if n<1:return 0
 if n<b>>1:return g(n,b>>1)
 return(g(b-1-n,b)+1)%4
n=int(input());A=[[1,0,0,0]];Z=[0]*4;K=(0,1,2,3);s=0
while sum(A[-1])<n:
 z=[0]*4
 for i in K:z[(i+1)%4]+=A[-1][i]+A[-1][(i+1)%4]
 A+=[z]
while n:
 z=A[b:=n.bit_length()-1];n^=1<<b;p=g(s,1<<s.bit_length());s|=1<<b
 for i in K:Z[(i+p)%4]+=z[i]
print(Z[0]-Z[2],Z[1]-Z[3])