from math import*;lcm=lambda a,b:a*b//gcd(a,b)
L,R,k,*a=map(int,open(0).read().split());C=[1];Z=0;L-=1
for i in a:
 for x in[*C]:C.append(z:=-lcm(x,i));Z+=(1-2*(z>0))*(R//abs(z)-L//abs(z))
print(Z)