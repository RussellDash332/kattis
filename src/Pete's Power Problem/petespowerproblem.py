B, x = input().split(); d = B.find('.'); x = int(x)
if d == -1: print(int(B)**x)
else: e = str(int(B.replace('.', ''))**x).zfill(999); p = len(B)-d-1; print(str(int(e[:-p*x]or'0'))+'.'+e[-p*x:])