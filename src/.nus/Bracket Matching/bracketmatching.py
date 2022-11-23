import sys
input()
b = input()
s = []
for p in b:
    if p in '([{':
        s.append(p)
    else:
        if not s or s[-1] != {')':'(', ']':'[', '}':'{'}[p]:
            print('Invalid')
            sys.exit(0)
        else:
            s.pop()
print(['Invalid', 'Valid'][int(len(s)==0)])