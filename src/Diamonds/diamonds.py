r,c=map(int,input().split());m=[['.']*c for _ in'.'*r]
for i in range(2,r-3,5):
 for j in range(0,c-1,4):m[i][v:=min(j+2,c-1)]=m[i+1][v]='X'
for j in range(0,c-1,4):m[-min(3,(r-3)or 2)][v:=min(j+2,c-1)]=m[-min(4,r-2)][v]='X'
print('\n'.join(map(''.join,m)))