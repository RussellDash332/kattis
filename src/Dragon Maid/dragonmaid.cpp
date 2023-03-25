#include <bits/stdc++.h>

#define pb push_back
#define qb pop_back
#define ph push_heap
#define qh pop_heap
#define ub upper_bound

using namespace std;
using ll = long long;
using vll = vector<ll>;
using hs = unordered_set<ll>;
using hm = unordered_map<ll, vll>;

const ll MAX = 2e5; // big enough :)

ll to_pair(ll a, ll b) { // increasing P, decreasing idx
    return MAX * a - b;
}

ll get_idx(ll p) {
    return (MAX - p % MAX) % MAX;
}

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    cout.tie(NULL);
    ll n, q, k, x, p, v, b;
    vll vv, tmp;
    hm h, a;
    hs s;

    // Preprocessing, overall O(n log n)
    cin >> n;
    for (int i = 1; i <= n; i++) { // O(n)
        cin >> p >> v;
        s.insert(v); // O(1)
        if (h.find(v) == h.end()) {h[v] = vll();}
        h[v].pb(to_pair(p, i)); // O(1)
    }
    for (ll i : s) {vv.pb(i);} // O(n) to collect distinct V values
    sort(vv.begin(), vv.end()); // O(n log n)
    for (ll v2 : vv) { // overall, O(n)
        vll to_add;
        for (ll i : h[v2]) {
            tmp.pb(-i);
            ph(tmp.begin(), tmp.end()); // O(1) since size is at most 10
            if (tmp.size() > 10) {
                qh(tmp.begin(), tmp.end());
                tmp.qb();
            }
        }
        for (ll t : tmp) {to_add.pb(-t);} // O(1) since size is at most 10
        sort(to_add.begin(), to_add.end(), greater<ll>()); // O(1) since size is at most 10
        a[v2] = to_add;
    }

    // Each query is O(k + log n)
    cin >> q;
    while (q--) {
        cin >> x >> k;
        if (x < vv[0]) {cout<<-1<<'\n';}
        else {
            tmp.clear();
            b = *(ub(vv.rbegin(), vv.rend(), x, [](int a, int b){return a>=b;})); // O(log n)
            vll* to_check = &(a[b]);
            for (int i = 0; i < min(k, (ll) to_check->size()); i++) {tmp.pb(get_idx((*to_check)[i]));} // O(k)
            if (tmp.empty()) {cout<<-1<<'\n';}
            else { // O(k)
                for (ll i : tmp) {cout<<i<<' ';}
                cout<<'\n';
            }
        }
    }
    return 0;
}