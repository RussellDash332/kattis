#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    vector<ll> V, L;
    ll B, H, N, T=1, Z=0, P=0, x1, y1, x2, y2, D, E;
    unordered_set<ll> X;
    cin >> B >> H >> N;
    vector<tuple<ll,ll,ll,ll>> Q, U;
    for (ll i=0; i<N; i++){
        cin >> x1 >> x2 >> y1 >> y2;
        X.insert(x1); X.insert(x2);
        Q.emplace_back(y2, -1, x1, x2);
        Q.emplace_back(y1, 1, x1, x2);
    }
    vector<ll> i2x(X.begin(), X.end());
    sort(i2x.begin(), i2x.end());
    unordered_map<ll,ll> x2i;
    for (ll i=0; i<i2x.size(); i++) x2i[i2x[i]] = i;
    for (ll i=0; i<i2x.size()-1; i++) L.push_back(i2x[i+1]-i2x[i]);
    while (T < L.size()) T *= 2;
    vector<ll> C(2*T, 0), S(2*T, 0), W(2*T, 0);
    for (ll i=0; i<L.size(); i++) W[T+i] = L[i];
    for (ll p=T-1; p>0; p--) W[p] = W[2*p]+W[2*p+1];
    sort(Q.begin(), Q.end());
    for (auto &[y, v, x1, x2] : Q){
        Z += (y-P)*S[1]; D = x2i[x1], E = x2i[x2]; P = y;
        U.emplace_back(1, 0, T, 0);
        while (!U.empty()){
            auto [p, s, l, b] = U.back(); U.pop_back();
            if (b) {
                if (C[p]) S[p] = W[p];
                else if (p<T) S[p] = S[2*p]+S[2*p+1];
                else S[p] = 0;
            } else {
                U.emplace_back(p, s, l, 1);
                if (D<=s && s<=E-l) C[p] += v;
                else {
                    if (E>s && s>D-l/2) U.emplace_back(2*p, s, l/2, 0);
                    if (E+l/2>s+l && s+l>D) U.emplace_back(2*p+1, s+l/2, l/2, 0);
                }
            }
        }
    }
    cout << B*H-Z;
    return 0;
}