N,*A=map(int,open(0).read().split());I=max(range(N),key=lambda x:A[x])
def f(l):return max(((A[i]-A[0])*(I+l)-(A[I]-A[0])*(i+l))/(I-i) for i in range(I)) < 4
l,h=0,I and 10**10
while l<h:
 if f(m:=(l+h)//2):h=m
 else:l=m+1
print(l)