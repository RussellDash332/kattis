from cmath import*;n,p=map(eval,input().split());s=0
for k in range(99):w=exp(.02j*pi*-~k);s+=w**(n%100)*(p/(1-w+w*p))**n/(w-1)
print((n/p-50.5+s.real)/20)