import sys

for line in sys.stdin:
    try:
        s, dna = line.strip().split()
    except:
        break

    s2 = set()
    for i in range(len(s)):
        s2.add(s[:i] + s[i+1:])

    s3 = set()
    for i in range(len(s) + 1):
        for j in 'ACGT':
            s3.add(s[:i] + j + s[i:])

    c1, c2, c3 = 0, 0, 0
    for i in range(len(dna)):
        if dna[i:i+len(s)] == s:
            c1 += 1
    for st in s2:
        for i in range(len(dna)):
            if dna[i:i+len(st)] == st:
                c2 += 1
    for st in s3:
        for i in range(len(dna)):
            if dna[i:i+len(st)] == st:
                c3 += 1
    print(c1, c2, c3)
