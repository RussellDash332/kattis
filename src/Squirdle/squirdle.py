words = ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy']
one, two, pos = [], [], [*range(5)]
for word in words:
    print('?', word)
    if (verdict:=input()) == '22222': exit(0)
    for i in range(5):
        if verdict[i] == '1': one.append(word[i])
        if verdict[i] == '2': two.append((word[i], i)), pos.remove(i)
    if len(one) + len(two) == 5: break
if len(one) + len(two) != 5: one.append('z')
while 1:
    s = ['']*5; pos = pos[1:] + pos[:1]
    for e, i in two: s[i] = e
    for e, i in zip(one, pos): s[i] = e
    word = ''.join(s); print('?', word)
    if (verdict:=input()) == '22222': exit(0)
    for i in pos.copy():
        if verdict[i] == '2': pos.remove(i), one.remove(word[i]), two.append((word[i], i))