#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    cout.tie(NULL);
    
    int limit = 2000000;
    int numDiv[limit + 1];
    int numDiffPF[limit + 1];
    
    for (int i = 0; i <= limit; i++) {
        numDiv[i] = 1;
        numDiffPF[i] = 0;
    }
    
    for (int p = 2; p <= limit; p++) {
        if (!numDiffPF[p]) { // p is guaranteed a prime
            for (int i = 2*p; i <= limit; i += p) { // all multiples of p up to limit
                numDiffPF[i]++;
                int temp = i, exp = 1;
                while (temp % p == 0) {
                    temp /= p;
                    exp++;
                }
                numDiv[i] *= exp;
            }
        }
    }
    
    int q, x;
    cin >> q;
    while (q--) {
        cin >> x;
        cout << numDiv[x] - numDiffPF[x] << '\n'; // endl is making it slow
    }

    return 0;
}