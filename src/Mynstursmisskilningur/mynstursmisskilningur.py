n=int(input());M=10**9+7;Z=0;P=[1];Q=250000002;I=[0]
for _ in range(n):P+=[P[-1]*5%M]
for i in P[1:]:I+=[pow(i-1,-1,M)]
for m in range(1,n+1):B=n//m-1;C=P[m-1];Z=(Z-m*((5*C-1)*Q*C*I[m]*(B*P[m*B]-~-P[m*B]*I[m])-~B*P[n//m*m-1]*~-P[n%m+1]*Q-m*C))%M
print(Z)