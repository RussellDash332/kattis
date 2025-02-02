S=input();p=Z=1;M=10**6+9;R=0
while p<len(S)-1:
 if S[p]=='o'!=S[p-1]==S[p+1]and S[p-1]not in'aeiou':R+=1;p+=1
 else:Z=(R+3)//2*Z%M;R=0
 p+=1
print((R+3)//2*Z%M)