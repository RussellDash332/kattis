R,C=map(int,input().split());M=[[*map(int,input().split())]for _ in'.'*(R+2)];Z=[C*['.']for _ in'.'*R]
for i in range(R):
 for j in range(C):
  if M[i][j]:
   Z[i][j]='X'
   for p in(0,1,2):
    for q in(0,1,2):M[i+p][j+q]-=1
print(['\n'.join(map(''.join,Z)),'impossible'][any(map(any,M))])