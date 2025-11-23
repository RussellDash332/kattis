from itertools import*;P=[]
for _ in'.'*int(input()):
 s=[*input()];c=[i for i in range(len(s))if s[i]<'0']
 for p in product(*(range(10)for _ in'.'*len(c))):
  for i,x in zip(c,p):s[i]=str(x)
  P+=[''.join(s)]
print(len(P),*P)