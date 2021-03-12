#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    int n,a,b,c,d,e,f,s,fx,fy;
    cin >> n;
    while (n--) {
        cin >> a >> d >> b >> e >> c >> f;

        // Basically ax + by = c and dx + ey = f
        s = 0; // number of solutions

        for (int x = 1; x <= max(c,f); x++) {
            if (c > a*x && f > d*x) {
                if ((c-a*x) % b == 0 && (f-d*x) % e == 0) {
                    int y = (c-a*x)/b;
                    if (y > 0 && d*x+e*y == f) {
                        s ++;
                        fx = x;
                        fy = y;
                    }
                }
            }
        }

        if (s == 1)
            cout << fx << " " << fy << endl;
        else
            cout << "?" << endl;
    }
    return 0;
}