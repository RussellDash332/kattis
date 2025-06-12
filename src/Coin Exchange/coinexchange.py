A,B,C,D,E,X=map(int,input().split())
def f(P,A=A,B=B,C=C,D=D,E=E,X=X):
 A-=3*P;B+=P
 while X:R=max((2*X-D+1)//2,0);q=min(max((3*R-E+3)//4,0),B//3);B-=3*q;E+=4*q;r=min(R,E//3);E-=3*r;D+=2*r;x=min(X,D//2);D-=2*x;B+=3*x;X-=x
 return C+A//5+B//3
a,b=0,A//3
while b-a>2:
 if f(μ:=b-(b-a)//3)<f(λ:=a+(b-a)//3):b=μ
 else:a=λ
print(max(map(f,range(max(a-9,0),min(b+9,A//3+1)))))