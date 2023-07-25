import sys; input = sys.stdin.readline

def gcd(a, b):
    while b: a, b = b, a%b
    return a

def solve(p, q, n):
    '''
    Initially we want to find X = (p mod q) + (2p mod q) + ... + (np mod q)
    Suppose Y = p//q + 2p//q + ... + np//q
    Then X + qY = n(n+1)p//2
    Suffices to find the value of Y instead
    '''
    def helper(p, q, n):
        if n == 0: return 0
        '''
        Note: p and q must be coprime!
        If n >= q, reduce n to n%q
            Suppose n = xq+r where x = n//q and r = n%q
            Assume (p//q + 2p//q + ... + qp//q) = M
            Based on https://math.stackexchange.com/questions/2433305/summation-of-floor-function-series, M = (p-1)(q-1)//2 + p
            Then,
            p//q + 2p//q + ... + np//q  = (p//q + 2p//q + ... + qp//q) + ((q+1)p//q + ... + (2q)p//q) + ... (((x-1)q+1)p//q + ... + (xq)p//q) + ... + ((xq+1)p//q + ... + (xq+r)p//q)
                                        = M + (M+pq) + (M+2pq) + ... + (M+(x-1)pq) + (xpr + [p//q + 2p//q + ... + rp//q])
                                        = xM + (x-1)xpq//2 + xpr + (p//q + 2p//q + ... + rp//q) -> recurse from n to n%q=r instead
        If p >= q, reduce (p,q) to (p%q,q)
            Suppose p = xq+r where x = p//q and r = p%q
            Then,
            p//q + 2p//q + ... + np//q  = (xq+r)//q + 2(xq+r)//q + ... + n(xq+r)//q
                                        = (x+r//q) + (2x+2r//q) + ... + (nx+nr//q)
                                        = (x + 2x + ... + nx) + (r//q, 2r//q + ... + nr//q)
                                        = n(n+1)x/2 + (r//q, 2r//q + ... + nr//q) -> recurse from p to p%q=r instead
        Otherwise, we know that p < q and n < q, you can take a look at Doctor Vogler's reply on the link below for the recurrence relation
        https://web.archive.org/web/20180326090519/http://mathforum.org/library/drmath/view/73120.html
        TLDR: p//q + 2p//q + ... + np//q = (np//q)*n - (q//p + 2q//p + ... + (np//q)q//p) -> pretty cool!
        '''
        if n >= q: x = n//q; r = n%q; M = (p-1)*(q-1)//2 + p; return x*M + (x-1)*x*p*q//2 + x*p*r + helper(p, q, r)
        if p >= q: return n*(n+1)*(p//q)//2 + helper(p%q, q, n)
        m = n*p//q
        return m*n-helper(q, p, m)
    d = gcd(p, q)
    print(n*(n+1)*p//2-q*helper(p//d, q//d, n))

for _ in range(int(input())): solve(*map(int, input().split()))