import sys
for l in sys.stdin:
    a, n = l.split(); a, n = list(map(ord, a[::-1])), int(n)
    b, s, o = [10 if i<58 else 26 for i in a], [i-48 if i<58 else i-65 if i<91 else i-97 for i in a], [48 if i<58 else 65 if i<91 else 97 for i in a]
    s[0] += n
    for i in range(len(s)-1): s[i+1] += (s[i]-s[i]%b[i])//b[i]; s[i] %= b[i]
    while s[-1] >= b[-1]: s.append((s[-1]-s[-1]%b[-1])//b[-1]-(b[-1]==26)), b.append(b[-1]), o.append(o[-1]); s[-2] %= b[-2]
    print(''.join(map(lambda x: chr(s[x]+o[x]), range(len(s))))[::-1])