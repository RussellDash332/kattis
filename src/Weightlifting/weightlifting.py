e,s,f=map(int,input().split());d=[0]*9**8
for i in range(1,e+1):d[i]=min(d[i-s]+d[i-f]+1,1e9)
print(min(200/d[e],225/(d[e]+1)))