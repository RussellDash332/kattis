#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using pii = pair<int, int>;

const ll MAX = 3e9; // big enough :)

ll to_pair(ll a, ll b) { // sorted by frequency, then descending element
    return MAX * (a + 1) - b;
}

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    cout.tie(NULL);
    
    int q, x, y, f, d;
    cin >> q;
    string cmd;
    deque<pii> dq;
    unordered_map<int, int> freq;
    set<ll> freq2;
    pii p;

    while (cin >> cmd) {
        if (cmd == "PUT_TOP") {
            cin >> x >> y;
            freq2.erase(to_pair(freq[y], y));
            freq[y] += x;
            freq2.insert(to_pair(freq[y], y));
            dq.push_front({x, y});
        } else if (cmd == "PUT_BOTTOM") {
            cin >> x >> y;
            freq2.erase(to_pair(freq[y], y));
            freq[y] += x;
            freq2.insert(to_pair(freq[y], y));
            dq.push_back({x, y});
        } else if (cmd == "REMOVE_TOP") {
            cin >> x;
            while (x != 0) {
                pii p = dq.front();
                d = min(p.first, x);
                dq.pop_front();
                if (p.first - d) {
                    dq.push_front({p.first - d, p.second});
                }
                freq2.erase(to_pair(freq[p.second], p.second));
                freq[p.second] -= d;
                x -= d;
                freq2.insert(to_pair(freq[p.second], p.second));
            }
        } else { // REMOVE_BOTTOM
            cin >> x;
            while (x != 0) {
                pii p = dq.back();
                d = min(p.first, x);
                dq.pop_back();
                if (p.first - d) {
                    dq.push_back({p.first - d, p.second});
                }
                freq2.erase(to_pair(freq[p.second], p.second));
                freq[p.second] -= d;
                x -= d;
                freq2.insert(to_pair(freq[p.second], p.second));
            }
        }
        cout << MAX - *freq2.rbegin() % MAX << "\n";
    }
    return 0;
}