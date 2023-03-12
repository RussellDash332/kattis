#include <bits/stdc++.h>

#define lb lower_bound

using namespace std;
using ll = long long;
using avl = set<ll>;

const ll MAX = 3e9; // big enough :)

ll to_pair(ll a, ll b) {
    return MAX * a + b;
}

ll get_a(ll p) {
    return p / MAX;
}

ll get_b(ll p) {
    return p % MAX;
}

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    cout.tie(NULL);
    
    int q;
    ll n, t, a, b, a2, b2, ans=0;
    avl intervals;
    cin >> n >> q;
    intervals.insert(0); // dummy
    intervals.insert(to_pair(n + 1, n + 1)); // dummy
    while (cin >> t) {
        if (t == 2) {
            cout << ans << '\n';
        } else {
            cin >> a >> b;
            if (intervals.find(to_pair(a, b)) == intervals.end()) {
                ans += (b-a+1);
                intervals.insert(to_pair(a, b));

                // Get set with equal start but smallest end
                avl::iterator i = intervals.lb(to_pair(a, 0));

                // Check previous if its endpoint > a
                // Only need to check once since the invariant is
                // that there are no overlaps at the beginning of each iter
                avl::iterator p = prev(i);
                if (*p != 0 && get_b(*p) >= a) {
                    i=p;
                    a=get_a(*i);
                }

                // Smallest element in the set that is affected
                a=get_a(*i);
                b=max(b, get_b(*i));
                while (i != intervals.end()) {
                    a2 = get_a(*i);
                    b2 = get_b(*i);
                    if (b >= a2) {
                        b = max(b, b2);
                        ans -= (b2-a2+1);
                        i = intervals.erase(i);
                    } else {
                        break;
                    }
                }

                // Reinsert final merged pair
                if (intervals.find(to_pair(a, b)) == intervals.end()) {
                    ans += (b-a+1);
                    intervals.insert(to_pair(a, b));
                }
            }
        }
    }
    return 0;
}