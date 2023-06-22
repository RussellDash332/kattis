#include <bits/stdc++.h>

using namespace std;
using vi = vector<int>;
using qi = queue<int>;
using vvi = vector<vector<int>>;
using vp = vector<pair<int, int>>;
using pii = pair<int, int>;
using hm = unordered_map<int, vector<int>>;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    cout.tie(NULL);
    
    vp delta = {pii(-1, 0), pii(1, 0), pii(0, 1), pii(0, -1)};
    int t, n, R, C, r, c, u, d, dr, dc, nr, nc;
    cin >> t;
    while (t--) {
        cin >> n >> R >> C;
        qi q;
        vvi D;
        hm M;
        for (int i = 0; i < R; i++) {
            D.push_back(vi(C, -1));
        }
        for (int i = 0; i < n; i++) {
            cin >> r >> c;
            D[r][c] = 0;
            q.push(r*C+c);
        }

        // BFS
        while (!q.empty()) {
            u = q.front();
            q.pop();
            r = u/C;
            c = u%C;
            d = D[r][c];
            for (pii p : delta) {
                dr = p.first;
                dc = p.second;
                nr = r+dr;
                nc = c+dc;
                if (0<=nr && nr<R && 0<=nc && nc<C) {
                    if (D[nr][nc] == -1) {
                        D[nr][nc] = d+1;
                        if (M.find(d+1) == M.end()) {
                            M[d+1] = vi();
                        }
                        M[d+1].push_back(nr*C+nc);
                        q.push(nr*C+nc);
                    }
                }
            }
        }

        if (M.empty()) {
            cout << R+C-2 << '\n';
        } else {
            int lo=0, hi=d, found, mid, x1, x2, y1, y2;
            while (lo <= hi) {
                found = 0;
                mid = (lo + hi)/2;
                if (M.find(mid) != M.end()) {
                    for (int u1 : M[mid]) {
                        for (int u2 : M[mid]) {
                            x1 = u1/C;
                            x2 = u2/C;
                            y1 = u1%C;
                            y2 = u2%C;
                            if (abs(x1-x2) + abs(y1-y2) >= mid) { found = 1; }
                            if (found) { break; }
                        }
                        if (found) { break; }
                    }
                }
                if (!found && mid != 0) { hi = mid-1; }
                else { lo = mid+1; }
            }
            cout << hi << '\n';
        }
    }

    return 0;
}