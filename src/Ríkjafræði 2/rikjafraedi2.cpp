#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N, Q;
    cin >> N >> Q;
    vector<bitset<1000>> G(N);
    int c, x, y;
    for (int i = 0; i < N; i++) G[i][i] = 1;
    while (Q--) {
        cin >> c >> x >> y;
        x--; y--;
        if (c) cout << (G[x][y] ? "Jebb" : "Neibb") << '\n';
        else for (int i = 0; i < N; i++) if (G[i][x]) G[i] |= G[y];
    }
    return 0;
}