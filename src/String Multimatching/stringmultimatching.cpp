// https://github.com/stevenhalim/cpbook-code/blob/master/ch6/sa_lcp.cpp
#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;

class SuffixArray {
private:
    vi RA;

    void countingSort(int k) {
        int maxi = max(300, n);
        vi c(maxi, 0);
        for (int i = 0; i < n; ++i)
            ++c[i+k < n ? RA[i+k] : 0];
        for (int i = 0, ss = 0; i < maxi; ++i) {
            int t = c[i]; c[i] = ss; ss += t;
        }
        vi temp(n);
        for (int i = 0; i < n; ++i)
            temp[c[SA[i]+k < n ? RA[SA[i]+k] : 0]++] = SA[i];
        swap(SA, temp);
    }

    void constructSA() {
        SA.resize(n);
        iota(SA.begin(), SA.end(), 0);
        RA.resize(n);
        for (int i = 0; i < n; ++i) RA[i] = T[i];
        for (int k = 1; k < n; k <<= 1) {
            countingSort(k);
            countingSort(0);
            vi temp(n);
            int r = 0;
            temp[SA[0]] = r;
            for (int i = 1; i < n; ++i)
                temp[SA[i]] =
                    ((RA[SA[i]] == RA[SA[i-1]]) && (RA[SA[i]+k] == RA[SA[i-1]+k])) ? r : ++r;
            swap(RA, temp);
            if (RA[SA[n-1]] == n-1) break;
        }
    }

public:
    string T;
    const int n;
    vi SA;

    SuffixArray(string initialT) : T(initialT), n(initialT.size()) {
        constructSA();
    }

    ii stringMatching(string P) {
        int m = (int)P.size();
        int lo = 0, hi = n-1;
        while (lo < hi) {
            int mid = (lo+hi) / 2;
            int res = T.compare(SA[mid], m, P);
            (res >= 0) ? hi = mid : lo = mid+1;
        }
        if (T.compare(SA[lo], m, P) != 0) return {-1, -1};
        ii ans; ans.first = lo;
        hi = n-1;
        while (lo < hi) {
            int mid = (lo+hi) / 2;
            int res = T.compare(SA[mid], m, P);
            (res > 0) ? hi = mid : lo = mid+1;
        }
        if (T.compare(SA[hi], m, P) != 0) --hi;
        ans.second = hi;
        return ans;
    }
};

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    cout.tie(NULL);

    int n, lo, hi;
    string p, s;
    ii ans;
    while (cin >> n) {
        cin.ignore();
        vector<string> pp;
        for (int i = 0; i < n; i++) {
            getline(cin, p); pp.push_back(p);
        }
        getline(cin, s);
        s += char(0);
        SuffixArray sa(s);
        for (int i = 0; i < n; i++) {
            ans = sa.stringMatching(pp[i]);
            lo = ans.first; hi = ans.second;
            if (lo+1 || hi+1) {
                vi v;
                for (int j = lo; j <= hi; j++) {
                    v.push_back(sa.SA[j]);
                }
                sort(v.begin(), v.end());
                for (int j : v) {
                    cout << j << ' ';
                }
                cout << endl;
            }
        }
    }
    return 0;
}