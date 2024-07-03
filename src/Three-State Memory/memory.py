a,b=1,0
for i in input()[::-1]:
 if i>'0':a+=b
 else:b+=a
print(a%(10**9+9))