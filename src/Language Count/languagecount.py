import re;K={}
for _ in'.'*int(input()):
 *_,c=re.sub('\(\w+\)','',input()).split()
 if c not in K:K[c]=0
 K[c]+=1
for i in sorted(K):print(i,K[i])