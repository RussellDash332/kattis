s=[]
for i in input().split():
 if i==')':
  k=[]
  while not k or k[-1]!='(':k+=[s.pop()]
  k.pop();p=k.pop()
  if p=='+':s+=[sum(k)]
  elif p=='/':s+=[k[1]//k[0]]
  else:s+=[k[1]-k[0]]
 else:s+=[int(i)if i.isdigit()else i]
print(*s)