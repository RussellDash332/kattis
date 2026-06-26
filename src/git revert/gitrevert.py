s=input();z=1
while s[:8]=='Revert "'!=s[-1]=='"':z^=1;s=s[8:-1]
print('un'*z+'revert')