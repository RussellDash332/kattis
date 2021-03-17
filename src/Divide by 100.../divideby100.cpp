#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    string n,m;
    cin >> n >> m;
    int z, d = (int) n.length(), k = (int) m.length()-1; // m = 10^k
    
    for (z = d-1; z >= 0; z--) {
        if (n[z] != '0')
            break;
    }
    
    // d-1-z = number of trailing zeroes

    if (k <= d-1-z) // trailing zeros > k
        cout << n.substr(0,d-k);
    else { // < k trailing zeros, e.g. 1230 / 1000
        if (d-k <= 0) {
            cout << "0.";
            for (int i = 0; i < k-d; i++)
                cout << 0;
            cout << n.substr(0,z+1);
        } else
            cout << n.substr(0,d-k) << "." << n.substr(d-k,k-d+1+z);
    }
    return 0;
}