#include <bits/stdc++.h>

#define INF INT_MAX
#define pb push_back
#pragma GCC optimize("Ofast,unroll-loops")
#pragma GCC target("avx,avx2,fma")

using namespace std;
using ll = long long;
using vll = vector<ll>;
using vvll = vector<vector<ll>>;
using pll = pair<ll, ll>;
using st = stack<pll>;

const ll MOD = 1e9+3233;

struct Node {
    ll sm, sM, smM, m, M, len;

    Node() {
        sm = 0; sM = 0; smM = 0;
        len = 0;
        m = INF;
        M = INF;
    }

    void setm(ll v) {
        sm = v*len%MOD;
        smM = v*sM%MOD;
        m = v;
    }

    void setM(ll v) {
        sM = v*len%MOD;
        smM = v*sm%MOD;
        M = v;
    }
};

struct E {
    int x, lo, hi;
};

struct Tree {
    int N, lo, hi;
    vector<Node> t;

    Tree(int n) {
        N = 1; lo = 0; hi = 0;
        while (N < n) N *= 2;
        t.resize(2*N);
        stack<E> s;
        s.push({1, 0, N});
        int x, l, h;
        while (!s.empty()) {
            x = s.top().x;
            l = s.top().lo;
            h = s.top().hi;
            s.pop();
            t[x].len = h-l;
            if (l+1 == h) continue;
            int m = (l+h)/2;
            s.push({2*x, l, m});
            s.push({2*x+1, m, h});
        }
    }

    void setM(int X, int L, int H, ll v) {
        stack<E> s;
        s.push({2*X, L, H});
        int x, xb, l, h, m;
        while (!s.empty()) {
            xb = s.top().x;
            l = s.top().lo;
            h = s.top().hi;
            s.pop();
            x = xb/2;
            if (!(xb%2)) {
                if (h <= lo || hi <= l) continue;
                if (lo <= l && hi >= h) {
                    t[x].setM(v); continue;
                }
                m = (l+h)/2;
                if (t[x].m != INF) {
                    t[2*x].setm(t[x].m); t[2*x+1].setm(t[x].m); t[x].m = INF;
                }
                if (t[x].M != INF) {
                    t[2*x].setM(t[x].M); t[2*x+1].setM(t[x].M); t[x].M = INF;
                }
                s.push({xb+1, l, h}); s.push({4*x, l, m}); s.push({4*x+2, m, h});
            } else {
                t[x].sm = (t[2*x].sm + t[2*x+1].sm) % MOD;
                t[x].sM = (t[2*x].sM + t[2*x+1].sM) % MOD;
                t[x].smM = (t[2*x].smM + t[2*x+1].smM) % MOD;
            }
        }
    }

    void setm(int X, int L, int H, ll v) {
        stack<E> s;
        s.push({2*X, L, H});
        int x, xb, l, h, m;
        while (!s.empty()) {
            xb = s.top().x;
            l = s.top().lo;
            h = s.top().hi;
            s.pop();
            x = xb/2;
            if (!(xb%2)) {
                if (h <= lo || hi <= l) continue;
                if (lo <= l && hi >= h) {
                    t[x].setm(v); continue;
                }
                m = (l+h)/2;
                if (t[x].m != INF) {
                    t[2*x].setm(t[x].m); t[2*x+1].setm(t[x].m); t[x].m = INF;
                }
                if (t[x].M != INF) {
                    t[2*x].setM(t[x].M); t[2*x+1].setM(t[x].M); t[x].M = INF;
                }
                s.push({xb+1, l, h}); s.push({4*x, l, m}); s.push({4*x+2, m, h});
            } else {
                t[x].sm = (t[2*x].sm + t[2*x+1].sm) % MOD;
                t[x].sM = (t[2*x].sM + t[2*x+1].sM) % MOD;
                t[x].smM = (t[2*x].smM + t[2*x+1].smM) % MOD;
            }
        }
    }
};

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    cout.tie(NULL);
    ll ans=0;
    int N;
    st D, I;
    D.push({INF, -1}); I.push({-INF, -1});
    cin >> N;
    vll X(N);
    Tree T(N);
    for (int i = 0; i < N; i++) {
        cin >> X[i];
        while (D.top().first < X[i]) D.pop();
        while (I.top().first > X[i]) I.pop();
        T.hi = i+1;
        T.lo = D.top().second+1; T.setM(1, 0, T.N, X[i]);
        T.lo = I.top().second+1; T.setm(1, 0, T.N, X[i]);
        D.push({X[i], i}); I.push({X[i], i});
        ans += T.t[1].smM; ans %= MOD;
    }
    cout << ans;
    return 0;
}