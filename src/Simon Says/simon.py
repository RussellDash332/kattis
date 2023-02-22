import sys
for l in sys.stdin:
    if l.startswith('simon says '): print(l.strip()[11:])
    else: print()