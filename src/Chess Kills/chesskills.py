Z=(range(1,8),range(-1,-8,-1));c=[input().split(',')for _ in' '*8];R={}
for i in range(8):
 for j in range(8):
  x=c[i][j];K=lambda i,j:8>i>-1<j<8!='x'==c[i][j]
  if x=='p':
   if K(i+1,j+1):R[x]=R.get(x,set())|{(i+1,j+1)}
   if K(i+1,j-1):R[x]=R.get(x,set())|{(i+1,j-1)}
  if x=='K':
   for a in range(-1,2):
    for b in range(-1,2):
     if K(i+a,j+b):R[x]=R.get(x,set())|{(i+a,j+b)}
  if x=='k':
   for a in range(-2,3):
    for b in range(-2,3):
     if a*a+b*b==5and K(i+a,j+b):R[x]=R.get(x,set())|{(i+a,j+b)}
  if x in'Qr':
   for r in Z:
    for a in r:
     if 8>i+a>-1:
      if K(i+a,j):R[x]=R[x]=R.get(x,set())|{(i+a,j)}
      if c[i+a][j]>' ':break
    for a in r:
     if 8>j+a>-1:
      if K(i,j+a):R[x]=R[x]=R.get(x,set())|{(i,j+a)}
      if c[i][j+a]>' ':break
  if x in'Qb':
   for r in Z:
    for a in r:
     if 8>i+a>-1<j+a<8:
      if K(i+a,j+a):R[x]=R.get(x,set())|{(i+a,j+a)}
      if c[i+a][j+a]>' ':break
    for a in r:
     if 8>i+a>-1<j-a<8:
      if K(i+a,j-a):R[x]=R[x]=R.get(x,set())|{(i+a,j-a)}
      if c[i+a][j-a]>' ':break
if not R:print('No Kills Possible');exit()
for i in sorted(R,key='KQkbrp'.index):print(f'{i}: {len(R[i])}')