n=int(input());b=sorted(map(int,input().split()));a,m=map(eval,input().split());s=sum(b);t=(2*s-a*n*(n-2))//n;h={*b};M=b[n//2]if n%2else(b[n//2-1]+b[n//2])/2
for i in b:
 if i>=t-i:break
 if t-i not in h:continue
 if n%2:
  if [i<M<t-i,M>=t-i,M<=i,][(m>0)-(m<0)]:print(i,t-i)
 else:
  p,A,B,q=b[n//2-2:n//2+2];U=2*(M+m)
  if any([U==B+q and i<A>=t-i,U==A+q and i<A<B==t-i,U==B+p and i==A<B<t-i,U==A+p and i>=B<t-i,U==p+q and i==A<B==t-i,m==0and i<A<B<t-i]):print(i,t-i)