N,M,*A=map(int,open(0).read().split())
def f(x):
 z=0
 for i in A:z+=i>x;x-=i*(i<=x)
 return z
print(min(map(f,range(M-10,M+1))))