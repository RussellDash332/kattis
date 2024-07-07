s = ''; p = q = 0; w = []
for i in range(27): s += chr(97+(i%26))*5
for _ in range(40):
    for _ in range(126): w.append(s[q:q+5]+s[p:p+5]); p = (p+1)%130
    p = (p-1)%130; q = (q+1)%130; w.append(s[q:q+5]+s[p:p+5]); q = (q+1)%130
for i in w[:int(input())]: print(i)