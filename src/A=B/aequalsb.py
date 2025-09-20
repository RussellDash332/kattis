S=input();R=[input().split('=')for _ in'.'*int(input())]
for i in range(5001):
 h=1
 for a,b in R:
  if a in S:S=S.replace(a,b,1);h=0;break
 if h:break
 if i>4999:print('Time Limit Exceeded')<exit()
 if len(S)>255:print('Memory Limit Exceeded')<exit()
print(S)