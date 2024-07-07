def add(word, verdict):
    temp = {}
    for idx in range(len(word)):
        if verdict[idx] != 'X':
            if word[idx] not in temp:
                temp[word[idx]] = 0
            temp[word[idx]] += 1
    for k in temp:
        if k not in freq:
            freq[k] = set(range(len(word)))
        freq[k] -= set(range(temp[k]))
    for idx in range(len(word)):
        if verdict[idx] == 'X':
            if word[idx] in temp:
                freq[word[idx]] = {temp[word[idx]]}
            else:
                freq[word[idx]] = {0}
    for idx in range(len(word)):
        if verdict[idx] == '/':
            if word[idx] not in kb:
                kb[word[idx]] = set(range(len(word)))
            kb[word[idx]] -= {idx}
    for idx in range(len(word)):
        if verdict[idx] == 'O':
            if word[idx] not in kb2:
                kb2[word[idx]] = set()
            kb2[word[idx]].add(idx)
    for idx in range(len(word)):
        if verdict[idx] == 'X' and word[idx] not in kb and word[idx] not in kb2:
            illegal.add(word[idx])

def verify(check):
    kb2c = {}
    for k in kb2:
        kb2c[k] = kb2[k].copy()
    for idx in range(len(check)):
        if check[idx] in illegal:
            return
        try:
            kb2c[check[idx]].remove(idx)
            if not kb2c[check[idx]]:
                del kb2c[check[idx]]
        except:
            if check[idx] in kb and idx not in kb[check[idx]]:
                return
    freq2 = {}
    for k in check:
        if k not in freq2:
            freq2[k] = 0
        freq2[k] += 1
    for k in freq2:
        if k in freq and freq2[k] not in freq[k]:
            return
    for k in freq:
        if k in freq2:
            if min(freq[k]) > freq2[k]:
                return
        elif min(freq[k]) > 0:
            return
    if not kb2c:
        possible.append(check)

from random import *
N = int(input()); W = [input() for _ in range(N)]
kb, kb2, freq = {}, {}, {}; illegal = set()
while W:
    print(word:=choice(W)); W.remove(word); verdict = input(); add(word, verdict)
    if verdict == 'O'*5: exit(0)
    possible = []
    for w in W: verify(w)
    W = possible