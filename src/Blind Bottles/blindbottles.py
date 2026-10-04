R=range;I=lambda:(print(*p),t:=int(input()),t==n<exit())[1];n=int(input());p=[*range(1,n+1)];s=I()
for i in R(n):
 for j in R(i):exec(w:='p[i],p[j]=p[j],p[i]');t=I();exec([w,'s=t'][t>s])