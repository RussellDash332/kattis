#include <bits/stdc++.h>

#define INF 1e7
using namespace std;

int dp[1<<20][22];
int G[22][22];
int points[22];
int ttime[22];
int ddl[22];
int n, T;

int f(int bm, int curr) {
    // explore all cities represented by bm, end up at curr
    if (bm&(1<<curr)) { // do task here
        int t = f(bm^(1<<curr), curr);
        return (t+ttime[curr] > ddl[curr]) ? INF : t+ttime[curr];
    } else if (!bm) {
        return G[n][curr]; // just go straight to it
    } else if (dp[bm][curr] != 2*INF) {
        return dp[bm][curr]; // memoize!
    } else {
        int r = INF;
        for (int i = 0; i < n; i++) { // try all cities you're not doing task on
            if (bm&(1<<i)) r = min(r, f(bm, i)+G[i][curr]);
        }
        return (dp[bm][curr]=r);
    }
}

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> T;
    for (int i = 0; i < (1<<n); i++)
        for (int j = 0; j < n+2; j++) dp[i][j] = 2*INF;
    for (int i = 0; i < n; i++) {
        cin >> points[i] >> ttime[i] >> ddl[i];
        if (ddl[i] == -1) ddl[i] = INF;
    }
    for (int i = 0; i < n+2; i++)
        for (int j = 0; j < n+2; j++) cin >> G[i][j];
    vector<int> c(n, 21);
    int best = 0;
    for (int i = 0; i < (1<<n); i++) {
        if (f(i, n+1) <= T) {
            int pt = 0;
            vector<int> cc;
            for (int j = 0; j < n; j++) {
                if (i&(1<<j)) {
                    pt += points[j];
                    cc.push_back(j+1);
                }
            }
            if (best < pt) {
                best = pt; c = cc;
            } else if (best == pt) {
                int update = 2;
                for (int i = 0; i < min(c.size(), cc.size()); i++) {
                    if (c[i] < cc[i]) {
                        update = 0; break;
                    } else if (c[i] > cc[i]) {
                        update = 1; break;
                    }
                }
                if (update == 2) update = (c.size() > cc.size()) ? 1 : 0;
                if (update) c = cc;
            }
        }
    }
    cout << best << '\n';
    if (best) for (int i : c) cout << i << ' ';
    return 0;
}