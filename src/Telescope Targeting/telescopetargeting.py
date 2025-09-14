W,H=map(int,input().split());A=[input()for _ in'.'*H]
w,h=map(int,input().split());B=[input()for _ in'.'*h]
for i in range(h-H+1):
 for j in range(w-W+1):
  if all(A[k][l]==B[i+k][j+l]for k in range(H)for l in range(W)):print(j-(w-W)//2,i-(h-H)//2)