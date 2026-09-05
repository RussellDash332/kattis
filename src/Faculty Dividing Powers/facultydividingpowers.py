from subprocess import*;from collections import*
for s in[*open(0)][1:]:
 n,k=map(int,s.split());z=10**18
 for p,e in Counter(map(int,check_output(f"factor {k}",shell=1).split()[1:])).items():
  m=n;s=0
  while m:s+=m//p;m//=p
  z=min(z,s//e)
 print(z)