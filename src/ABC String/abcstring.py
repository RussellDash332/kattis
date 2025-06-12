v=[0]*7
for i in input():
 x=2**(ord(i)-65)
 for j in range(6,-1,-1):
  if v[j]and j&x<1:v[j]-=1;v[(j+x)%7]+=1;break
 else:v[x]+=1
print(v[0])