from fractions import*;t,s=map(int,input().split());T=S=0
for i in range(s):S+=max(v:=s+min(-i//2,s-2*i),0);T+=max(min(t-i,v),0)
print(Fraction(4*T+1,4*S+1))