from random import *; seed(1337)
S = {}; L = {}
for _ in range(int(input())):
    s, e = map(int, input().split())
    if s > e: S[s] = e
    else: L[s] = e
curr = [input(), 0]; nxt = [input(), 0]
while True:
    r = randint(1, 6); curr[1] = min(curr[1]+r, 100)
    print(f'{curr[0]} rolled {r} and is now at square {curr[1]}.')
    if curr[1] in S: curr[1] = S[curr[1]]; print(f'Darn! A snake brought {curr[0]} down to square {curr[1]}.')
    elif curr[1] in L: curr[1] = L[curr[1]]; print(f'Splendid! {curr[0]} climbed a ladder up to square {curr[1]}.')
    if curr[1] > 99: print(curr[0], 'won the game.'); break
    if r < 6: curr, nxt = nxt, curr