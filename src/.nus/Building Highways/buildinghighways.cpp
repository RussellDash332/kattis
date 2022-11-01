#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    cout.tie(NULL);
    long long n, q, s = 0, m = 1E7;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> q;
        m = min(m, q);
        s += q;
    }
    cout << m * (n - 2) + s;
    return 0;
}