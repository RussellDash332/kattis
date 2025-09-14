R=range(-2,3)
for _ in'.'*int(input()):
 r,c=map(int,input().split());m=[input()for _ in'.'*r];v={0};z=1
 for j in range(c):
  if m[-1][j]=='*':q=[(r-1,j,r-1,j)]
 while q:
  i,j,k,l=q.pop()
  if(i,j,k,l)in v:continue
  if i==0:z=0;break
  v.add((i,j,k,l));q.extend((i+x,j+y,k,l)for x in R for y in R if r>i+x>-1<j+y<c and m[i+x][j+y]in'HB'and k-2<i+x<=k and abs(j+y-l)<2);q.extend((i,j,k+x,l+y)for x in R for y in R if r>k+x>-1<l+y<c and m[k+x][l+y]in'FB'and i<=k+x<i+2 and abs(j-y-l)<2)
 print('Not '*z+'Climbable')