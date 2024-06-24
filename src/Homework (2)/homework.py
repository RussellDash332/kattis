import sys; input = sys.stdin.readline; from array import *
s = input().strip(); s1 = input().strip(); s2 = input().strip(); dp = array('b', [1]+[0]*len(s2))
for i in range(1, len(s2)+1): dp[i] = s[i-1] == s2[i-1]
for i in range(len(s1)):
    for j in range(1, len(s2)+1): dp[j] = (dp[j] and s[i+j] == s1[i]) or (dp[j-1] and s[i+j] == s2[j-1])
print('yneos'[1-dp[-1]::2])