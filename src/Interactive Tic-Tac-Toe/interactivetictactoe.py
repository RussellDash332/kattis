from sys import stdin

class State:
    mem = {}
    def __init__(self, b, t):
        self.b, self.c, self.t = b, [b[::4],b[1::4],b[2::4],b[::5],b[2::3]]+b.split(), t
    def check(self):
        mem = State.mem
        if (self.b, self.t) in mem: return mem[(self.b, self.t)]
        x_win = 'xxx' in self.c
        o_win = 'ooo' in self.c
        assert not (x_win and o_win)
        mem[(self.b, self.t)] = 1 if x_win else -1 if o_win else 0
        return mem[(self.b, self.t)]
    def end(self):
        return self.check() or '.' not in self.b
    def nxt(self):
        s = []
        r = [list(i) for i in self.b.split()]
        for i in range(3):
            for j in range(3):
                if r[i][j] == '.':
                    r[i][j] = 'ox'[self.t]
                    s.append(State('\n'.join(''.join(w) for w in r), 1-self.t))
                    r[i][j] = '.'
        return s
    def out(self):
        print(self.b)

def max_value(state, alpha, beta, depth):
    if state.end() or depth == 0: return state.check(), None
    v = -float('inf')
    for a in state.nxt():
        v2, _ = min_value(a, alpha, beta, depth-1)
        if v2 > v:
            v, move = v2, a
            alpha = max(alpha, v)
        if v >= beta: return v, move
    return v, move

def min_value(state, alpha, beta, depth):
    if state.end() or depth == 0: return state.check(), None
    v = float('inf')
    for a in state.nxt():
        v2, _ = max_value(a, alpha, beta, depth-1)
        if v2 < v:
            v, move = v2, a
            beta = min(beta, v)
        if v <= alpha: return v, move
    return v, move

def get_b(): return State('\n'.join(input().strip() for _ in range(3)), 1)

turn = input().strip()
while True:
    b = get_b()
    assert len(b.b) == 11
    if b.end(): break
    value, move = max_value(b, -float('inf'), float('inf'), depth=9)
    move.out()
    if move.end(): break