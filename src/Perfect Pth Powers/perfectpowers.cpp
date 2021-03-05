#include <iostream>
#include <map>
#include <algorithm>
using namespace std;

int main()
{
    while (true) {
        long n;
        bool negative = false;

        map<long,int> factormap;
        cin >> n;
        
        if (n == 0) {
            break;
        } else if (n*n == 1) {
            cout << 31 << endl;
            continue;
        } else if (n < -1) {
            negative = true;
            n = -n;
        }
        
        long i = 2;
        while (i*i <= n) {
            if (n % i == 0) {
                n /= i;
                factormap[i]++;
            } else {
                i++;
            }
        }
        factormap[n]++;
        
        int ans = 100;
        for ( const auto &p : factormap ) {
            ans = min(ans,p.second);
            ans = __gcd(ans,p.second);
        }

        int ans2 = ans;
        while (ans2 % 2 == 0) {
            ans2 /= 2;
        }
        
        cout << ((negative && (ans % 2 == 0)) ? ans2 : ans) << endl;
    }
    return 0;
}