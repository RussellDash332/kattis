N=4**9;F=[0]*N
def f(i,v):
 while i<N:F[i]+=v;i+=i&-i
for s in[*open(0)][1:]:
 l,r=map(int,s.split());a=b=0;L=l;R=r
 while L:a-=F[L];L-=L&-L
 while R:b+=F[R];R-=R&-R
 print(b-a);f(l+1,1-a);f(r,~b);f(l,a);f(r+1,b)