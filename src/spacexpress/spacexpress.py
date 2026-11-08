for _ in range(int(input())):
    input(); S = [0]*676; C = [0]*676
    for i in range(26): S[27*i] = C[27*i] = 1
    for _ in range(int(input())): a, b = input().split(); S[26*ord(a)+ord(b)-1755] = S[26*ord(b)+ord(a)-1755] = 1
    for _ in range(int(input())): a, b = input().split(); C[26*ord(a)+ord(b)-1755] = C[26*ord(b)+ord(a)-1755] = 1
    for k in range(26):
        for i in range(26):
            for j in range(26): S[26*i+j] |= S[26*i+k]*S[26*k+j]; C[26*i+j] |= C[26*i+k]*C[26*k+j]
    print('YNEOS'[S!=C::2])