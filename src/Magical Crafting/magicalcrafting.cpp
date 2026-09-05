#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int C;
    cin >> C;
    for (int tc = 0; tc < C; tc++) {
        int N, M;
        cin >> N >> M;
        vector<tuple<int, int, int>> R[26];
        cout << "CASE #" << tc + 1 << "\n";
        for (int _ = 0; _ < N; _++) {
            char a, b, c; int w;
            cin >> a >> b >> c >> w;
            R[a-65].push_back({b-65, c-65, w});
        }
        for (int _ = 0; _ < M; _++) {
            int N; string ss;
            cin >> N >> ss;
            vector<int> s(N);
            for (int i = 0; i < N; i++) s[i] = ss[i]-97;
            vector<int> D(N*N*26, 1e9);
            for (int i = 0; i < N; i++) D[i*(N+1)*26+s[i]] = 1;
            for (int l = 2; l <= N; l++) {
                for (int i = 0; i <= N-l; i++) {
                    int j = i+l-1;
                    for (int a = 0; a < 26; a++) {
                        int z = 1e9;
                        for (int k = i; k < j; k++)
                            for (auto& [b, c, w] : R[a]) z = min(z, w+D[i*26*N+k*26+b] + D[(k+1)*26*N+j*26+c]);
                        D[i*26*N+j*26+a] = z;
                    }
                }
            }
            int Z = D[26*(N-1)];
            if (Z < 1e9) cout << "POSSIBLE WITH " << Z << " DIAMONDS\n";
            else cout << "IMPOSSIBLE\n";
        }
    }
    return 0;
}