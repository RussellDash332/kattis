#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main() {
    ll n, m, k;
    cin >> n >> m >> k;
    vector<ll> D(16*301*301, 1e9);
    for (int a = 1; a <= n; ++a) for (int b = 1; b <= m; ++b) for (int c = 0; c < 15; ++c) {
        ll v = (a*b-k)*(a*b-k);
        for (int i = 1; i < a; ++i) v = min(v, D[4816*i+16*b+(c|1)]+D[4816*(a-i)+16*b+(c|2)]);
        for (int i = 1; i < b; ++i) v = min(v, D[4816*a+16*i+(c|4)]+D[4816*a+16*(b-i)+(c|8)]);
        D[4816*a+16*b+c] = v;
    }
    cout << D[4816*n+16*m] << endl;
    return 0;
}