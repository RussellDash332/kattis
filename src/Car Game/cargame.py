import sys; input = sys.stdin.readline; from array import *
n, m = map(int, input().split()); a = []; r = array('i', [-1]*17576)
for t in range(n):
    p = [0]*26; q = [0]*676; s = input().strip(); a.append(s+'\n'); s = [*map(ord, s)]
    for i in s:
        i -= 97
        for j in range(26):
            for k in range(26):
                if q[26*j+k] != 0 and r[676*j+26*k+i] == -1: r[676*j+26*k+i] = t
            if p[j] != 0: q[26*j+i] = 1
        p[i] = 1
a.append('No valid word\n')
for _ in range(m): s = [*map(ord, input())]; sys.stdout.write(a[r[676*s[0]+26*s[1]+s[2]-45695]])