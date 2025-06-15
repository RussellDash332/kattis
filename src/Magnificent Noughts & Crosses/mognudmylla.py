NEXT_CACHE = {}
class State:
    def __init__(self, board='.'*9, x_left=4, X_left=2, o_left=4, O_left=2, turn=0):
        self.board = board; self.x_left = x_left; self.X_left = X_left; self.o_left = o_left; self.O_left = O_left; self.turn = turn
    def __repr__(self):
        return f'({self.board}, x={self.x_left}, X={self.X_left}, o={self.o_left}, O={self.O_left}, turn={self.turn})'
    def print(self):
        print(self.board[:3]), print(self.board[3:6]), print(self.board[6:])
    def check(self):
        # horizontal
        for i in range(3):
            s = self.board[3*i:3*i+3].lower()
            if s == 'xxx': return 1
            if s == 'ooo': return -1
        # vertical
        for i in range(3):
            s = self.board[i::3].lower()
            if s == 'xxx': return 1
            if s == 'ooo': return -1
        # diagonal
        s = self.board[::4].lower()
        if s == 'xxx': return 1
        if s == 'ooo': return -1
        s = self.board[2:7:2].lower()
        if s == 'xxx': return 1
        if s == 'ooo': return -1
        # no moves
        if not self.next(): return 2*self.turn-1
        return 0
    def next(self):
        key = (self.board, self.x_left, self.X_left, self.o_left, self.O_left, self.turn)
        if key in NEXT_CACHE: return NEXT_CACHE[key]
        result = []
        # fill empty space
        for i in range(9):
            if self.board[i] == '.':
                if self.turn == 0:
                    if self.x_left: result.append(State(self.board[:i]+'x'+self.board[i+1:], self.x_left-1, self.X_left, self.o_left, self.O_left, 1-self.turn))
                    if self.X_left: result.append(State(self.board[:i]+'X'+self.board[i+1:], self.x_left, self.X_left-1, self.o_left, self.O_left, 1-self.turn))
                else:
                    if self.o_left: result.append(State(self.board[:i]+'o'+self.board[i+1:], self.x_left, self.X_left, self.o_left-1, self.O_left, 1-self.turn))
                    if self.O_left: result.append(State(self.board[:i]+'O'+self.board[i+1:], self.x_left, self.X_left, self.o_left, self.O_left-1, 1-self.turn))
        # replace any lowercase with new/existing uppercase
        # no use replacing own lowercase, so only consider o->X and x->O
        ups = []; downs = []; b = [*self.board]; U = 'XO'[self.turn]
        for i in range(9):
            if self.board[i] == U: ups.append(i)
            if self.board[i] in 'ox': downs.append(i)
        for u in ups:
            for d in downs: z = b[d]; b[u], b[d] = '.', U; result.append(State(''.join(b), self.x_left, self.X_left, self.o_left, self.O_left, 1-self.turn)); b[u], b[d] = U, z
        for d in downs:
            if self.turn == 0 and self.X_left: result.append(State(self.board[:d]+'X'+self.board[d+1:], self.x_left, self.X_left-1, self.o_left, self.O_left, 1-self.turn))
            if self.turn == 1 and self.O_left: result.append(State(self.board[:d]+'O'+self.board[d+1:], self.x_left, self.X_left, self.o_left, self.O_left-1, 1-self.turn))
        NEXT_CACHE[key] = result; return result

def mm(state, depth=0):
    if depth == 2: return 0
    key = (state.board, state.x_left, state.X_left, state.o_left, state.O_left, state.turn)
    if key in MM_CACHE: return MM_CACHE[key]
    v = state.check()
    if v: MM_CACHE[key] = v; return v
    z = -10**9 if state.turn == 0 else 10**9
    for s in state.next():
        if state.turn == 0:
            z = max(z, mm(s, depth+1))
            if z > 0: break
        else:
            z = min(z, mm(s, depth+1))
            if z < 0: break
    MM_CACHE[key] = z; return z

def best(state):
    u = -10**9; b = None
    for s in state.next():
        c = mm(s)
        if c > u: u, b = c, s
    return b

MM_CACHE = {}
state = State().next()[9] # X in the middle
state.print()
while True:
    try:
        b = input()
        if '!' in b: break # game over, win
        b += input()+input()
    except:
        break
    nxt = None
    for s in state.next():
        if s.board == b: nxt = s; break
    MM_CACHE = {}
    state = best(nxt)
    state.print()