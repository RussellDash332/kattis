import sys; input = sys.stdin.readline
words = [{input().strip() for _ in range(int(input()))}]
pwds = [l.strip() for l in sys.stdin]
for _ in range(3):
    words2 = set()
    for word in words[-1]:
        for i in range(len(word)-1):
            if word[i] != word[i+1]: words2.add(word[:i]+word[i+1]+word[i]+word[i+2:]) # swap two adjacent
    words.append(words2)
spwd = set(pwds)
for pwd in pwds:
    dig = 0
    for i in pwd: dig += i.isdigit()
    if dig > 3: continue
    for k in range(4-dig):
        for w in words[k]:
            if len(w) != len(pwd): continue
            possible = True
            for i in range(len(w)):
                if w[i] != pwd[i] and pwd[i].isalpha(): possible = False; break
            if possible: spwd.discard(pwd); break
        if pwd not in spwd: break
for i in pwds:
    if i in spwd: print(i)