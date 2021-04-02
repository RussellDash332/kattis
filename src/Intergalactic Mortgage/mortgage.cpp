#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    double x=1,y=1,n=1,r=1;
    while (x != 0 || y != 0 || n != 0 || r != 0) {
        cin >> x >> y >> n >> r;
        if (x == 0 && y == 0 && r == 0 && n == 0)
            return 0;

        if (r != 0.00) {
            r /= 1200;
            n *= 12;
            double i = pow(1+r,n);
            cout << (r*x <= y*(1-1/i) ? "YES" : "NO") << endl;
        } else // zero interest
            cout << (x <= y*12*n ? "YES" : "NO") << endl;
    }

    return 0;
}