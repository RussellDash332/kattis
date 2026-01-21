import sys;sys.setrecursionlimit(10**5);P=sys.stdout.write;t=[]
for i in range(len(s:=open(0).read().split())):
 t.append(i)
 if s[i]in'+-*/':a,b=t.pop(),t.pop();t.append([t.pop(),a,b])
def F(t):
 if type(t)==int:P(s[t])
 elif type(t[0])==type(t[1])==type(t[2])==int:P('('+s[t[0]]+s[t[1]]+s[t[2]]+')')
 else:P('(');F(t[0]);P(s[t[1]]);F(t[2]);P(')')
F(t[0])