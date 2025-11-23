Z=[-1,0,0]
for s in open(0):
 try:Z[1-bytes(int(s[i:i+2],16)for i in range(0,len(s.strip()),2)).decode().isascii()]+=1
 except:Z[2]+=1
print(*Z)