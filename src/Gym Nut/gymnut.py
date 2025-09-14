from functools import*
@cache
def f(i,s,p):return max(min(E:=s*c**p,x[i])+f(i+1,E,1),f(i+1,e,0))if i-n else 0
e,n,c,*x=map(eval,open(z:=0).read().split());print(f(0,e,0))