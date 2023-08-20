#include <bits/stdc++.h>

#define INF 1e7
using namespace std;

int G[20][20];
int C[20971520];
int C2[20971520];
int rev[524288];

int dp1(int s, int bm, int n) {
    if (C[bm*n+s] != INF) return C[bm*n+s];
    if (!bm) return G[s][0];
    int bm2=bm, ans=INF, nxt, u;
    while (bm2) {
        nxt = bm2&-bm2;
        u = rev[nxt];
        ans = min(ans, G[s][u]+dp1(u, bm^nxt, n));
        bm2 -= nxt;
    }
    return (C[bm*n+s]=ans);
}

int dp2(int s, int bm, int n) {
    if (C2[bm*n+s] != INF) return C2[bm*n+s];
    if (!bm) return G[s][n-1];
    int bm2=bm, ans=INF, nxt, u;
    while (bm2) {
        nxt = bm2&-bm2;
        u = rev[nxt];
        ans = min(ans, G[s][u]+dp2(u, bm^nxt, n));
        bm2 -= nxt;
    }
    return (C2[bm*n+s]=ans);
}

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    cout.tie(NULL);
    int n, m, a, b, w, tc=0, ans, full, idx[20], ptr;
    for (int i = 0; i < 20; i++) rev[1<<i] = i+1; // precalc rev
    while (cin >> n >> m) {
        // set up graph and dp
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) G[i][j] = INF;
            G[i][i] = 0;
        }
        for (int i = 0; i < (n<<n); i++) C[i] = INF;
        // populate graph
        for (int i = 0; i < m; i++) {
            cin >> a >> b >> w;
            G[a][b] = G[b][a] = w;
        }
        // floyd-warshall
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) G[i][j] = min(G[i][j], G[i][k]+G[k][j]);
            }
        }
        if (n == 3) {
            cout << "Case " << ++tc << ": " << 2*(G[0][1]+G[1][2]) << '\n'; 
        } else {
            fill(begin(C), begin(C)+(n<<n), INF);
            fill(begin(C2), begin(C2)+(n<<n), INF);
            ans = INF;
            full = 1<<(n-2);
            for (int bm = 0; bm < full; bm++) {
                if (__builtin_popcount(bm) != n/2-1) continue;
                ptr = 0;
                for (int i = 0; i < n; i++) {
                    if (bm&(1<<i)) idx[ptr++] = i;
                }
                for (int i = 0; i < ptr; i++) {
                    for (int j = 0; j < ptr; j++) ans = min(ans, dp2(idx[i]+1, full-1-bm, n)+dp1(idx[i]+1, bm^(1<<idx[i]), n)+dp2(idx[j]+1, bm^(1<<idx[j]), n)+dp1(idx[j]+1, full-1-bm, n));
                }
            }
            cout << "Case " << ++tc << ": " << ans << '\n'; 
        }
    }
    return 0;
}