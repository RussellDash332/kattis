import sys; input = sys.stdin.readline; from collections import *
while 1:
    try: Q = int(input())
    except: break
    S = ''; z = 0
    while (s:=input().strip()) != 'IAMIRONMAN': S += ''.join(x if 'a'<=x<='z' else ' ' for x in s.lower())+' '
    for k, v in sorted(Counter(S.split()).items()):
        if v == Q: print(k); z = 1
    if 1-z: print('Guess there is no such thing as a Starkism.')