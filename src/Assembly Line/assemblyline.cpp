#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;

const int INF = 1e9;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N;
    cin >> N;
    char A[N], dmp, r;
    unordered_map<int, int> H;
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
        H[A[i]] = i;
    }
    vector<vector<int>> R(N);
    int C[N*N], c, Q;
    for (int i = 0; i < N*N; ++i) {
        cin >> c;
        cin >> dmp;
        cin >> r;
        R[H[r]].push_back(i);
        C[i] = c;
    }
    cin >> Q;
    while (Q--) {
        string s;
        cin >> s;
        int T = s.size(), U = N*T, D[U*T], ans;
        vector<int> S(T);
        for (int i = 0; i < T; ++i) S[i] = H[s[i]];
        pair<int, int> B = {INF, -1};
        for (int l = 0; l < T; ++l) {
            for (int i = 0; i < T-l; ++i) {
                for (int k = 0; k < N; ++k) {
                    if (l == 0) {
                        D[U*i+N*i+k] = (S[i] == k) ? 0 : INF;
                        continue;
                    }
                    ans = INF;
                    for (int m = i; m < i+l; ++m)
                        for (auto ab : R[k]) ans = min(ans, D[U*i+N*m+ab/N]+D[U*(m+1)+N*(i+l)+ab%N]+C[ab]);
                    D[U*i+N*(i+l)+k] = ans;
                }
            }
        }
        for (int k = 0; k < N; ++k) B = min(B, {D[U-N+k], k});
        cout << B.first << "-" << A[B.second] << "\n";
    }
    return 0;
}
