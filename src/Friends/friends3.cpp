#include <bits/stdc++.h>
#define lb lower_bound
#define FOR(n) for(int i = 0; i < n; ++i)
using namespace std;
#define ll long long

const ll M = 1e9+7;
static set<ll> T;
static ll Z;

void add(ll x) {
    auto s = T.lb(x*M+x);
    auto p = T.lb(x*M+x);
    ll a = x, b = x;
    if (p != T.begin()) p--;
    if (p != T.end() && (*p)%M == x-1) {
        ll v = *p;
        T.erase(p);
        Z -= (v%M-v/M+1)*(v%M-v/M+1);
        a = v/M;
    }
    if (s != T.end() && (*s)/M == x+1) {
        ll v = *s;
        T.erase(s);
        Z -= (v%M-v/M+1)*(v%M-v/M+1);
        b = v%M;
    }
    T.insert(a*M+b);
    Z += (b-a+1)*(b-a+1);
}

void remove(ll x) {
    auto p = T.lb(x*M+M-1);
    p--;
    ll v = *p;
    T.erase(p);
    ll a = v/M, b = v%M;
    Z -= (b-a+1)*(b-a+1);
    if (x > a) {
        Z += (x-a)*(x-a);
        T.insert(a*M+x-1);
    }
    if (x < b) {
        Z += (b-x)*(b-x);
        T.insert((x+1)*M+b);
    }
}

void init(int N, int L, int P[]) {
    FOR(N) add(P[i]);
}

void jump(int A, int B) {
    remove(A); add(B);
}

ll score() {
    return Z;
}