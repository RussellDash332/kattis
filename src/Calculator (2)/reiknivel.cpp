#include <bits/stdc++.h>
using namespace std;
int main() {
    int a, x, R = 1, P = 0, z;
    cin >> a >> x;
    vector<tuple<int, int, int>> K;
    for (int i = 0; i < a; i++) {
        string ops;
        int y, c;
        cin >> ops >> y >> c;
        int op = string("+-*/").find(ops);
        if ((op < 2 && y == 0) || (op > 1 && y == 1)) continue;
        K.emplace_back(op, y, c);
    }
    vector<int> D(1e8, 1e9);
    D[0] = 0;
    deque<int> Q[4];
    Q[0].push_back(0);
    while (R) {
        while (!Q[P%4].empty()) {
            int v = Q[P%4].front();
            Q[P%4].pop_front();
            R--;
            if (v == x) {
                cout << P << endl;
                return 0;
            }
            if (D[v] != P) continue;
            for (auto& [op, y, c] : K) {
                if (op == 0) z = v+y;
                else if (op == 1) z = v-y;
                else if (op == 2) z = v*y;
                else z = v/y;
                if (z < 0 || z >= 1e8) continue;
                if (D[z] > D[v]+c) {
                    D[z] = D[v]+c;
                    Q[(P+c)%4].push_back(z);
                    R++;
                }
            }
        }
        P++;
    }
    cout << "Engin leid!" << endl;
    return 0;
}