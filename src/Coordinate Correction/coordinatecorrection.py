from math import*;s,*v=open(0);n,d=map(int,s.split());p=lambda k:print(k.real,k.imag)
for a,b in zip(v:=[eval(i.replace(' ','+1j*'))for i in v],v[1:]):
 for i in range(k:=ceil(abs(t:=b-a)/d)):p(a+i*t/k)
p(b)