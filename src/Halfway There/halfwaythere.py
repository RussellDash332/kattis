s='.'.join((input()+'.0').split('.')[:2]);d=s.find('.');b=[0]*9
for i in s.replace('.','').strip('-'):b+=[0];k=5*int(i);b[-2]+=k//10;b[-1]+=k%10
e=~d+len(s);t=''.join(map(str,b));l=t[:~e].lstrip('0')or'0';r=t[~e:].rstrip("0");print(f'{"-"*(s[0]=="-")}{l}{"."+r if r else""}')