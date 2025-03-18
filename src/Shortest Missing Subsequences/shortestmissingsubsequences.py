import sys; input = sys.stdin.readline
k = input().strip()
s = [-1]+[ord(i)-97 for i in input().strip()]
z = b = 0; r = 1
for i in k: z |= 1<<(ord(i)-97)
a = [[-1]*26 for _ in s]
for i in range(1, len(s)):
    b |= 1<<s[i]
    if b == z: r, b = r+1, 0
    for j in range(i-1, -1, -1):
        a[j][s[i]] = i
        if s[j]==s[i]: break
for _ in range(int(input())):
    q = input().strip(); p = 0
    for i in q:
        p = a[p][ord(i)-97]
        if p == -1: break
    print(int(p==-1<len(q)==r))