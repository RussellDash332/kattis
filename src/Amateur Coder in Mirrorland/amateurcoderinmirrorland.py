from re import*;s=input()[::-1];K=[('left','right'),('up','down'),('in','out')];F=lambda x:r'\b'+x+r'\b'
for a,b in K:s=sub(F(b),a,sub(F(a),'@',s)).replace('@',b)
print(s)