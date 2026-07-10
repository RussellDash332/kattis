from bisect import*;A=[]
for i in range(N:=int(input())):t,x=map(int,input().split());A+=[(t-x,t+x,i)]
B=[];Z=[0]*N
for x,y,i in sorted(A):
 y=-y;p=bisect(B,y-1);Z[i]=p+1
 if p<len(B):B[p]=y
 else:B+=[y]
print(len(B),*Z)