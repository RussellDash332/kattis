M=10**9+7;E,L,R=map(int,open(0));S=[1]*(R+1);p=3;Z=1+(L<=2<=R)
while p<=R:
 if S[p]:
  S[p]=0;q=p*p
  if L<=p<=R:Z=Z*p%M
  while q<=R:S[q]=0;q+=2*p
 p+=2
print(pow(Z,E,M))