#include <bits/stdc++.h>
using namespace std;

int C[151][151][51] {{{0}}};

int dp(int N, int n5, int n10, int total) {
    for (int n = 1; n <= N; n++) {
        for (int i = 0; i <= n5 + n10; i++) {
            for (int j = 0; j <= n10; j++) {
                int mc = INT_MAX;

                // n1 from input can be recovered here
                int n1 = total - 5*i - 10*j;
                
                // Can I buy a coke with 8 1c coins?
                if (n1 >= 8)
                    mc = min(mc, C[n-1][i][j] + 8);
                
                // Can I buy a coke with 3 1c and 1 5c coins?
                if (i >= 1 && n1 >= 3)
                    mc = min(mc, C[n-1][i-1][j] + 4);
                
                // Can I buy a coke with 2 5c coins?
                if (i >= 2)
                    mc = min(mc, C[n-1][i-2][j] + 2);
                
                // Can I buy a coke with 1 10c coin?
                if (j >= 1)
                    mc = min(mc, C[n-1][i][j-1] + 1);
                
                // Can I buy 2 cokes with (1+1+1+10 -> 1coke+5 and 5+1+1+1-> 1coke)?
                // Compare this with 8 1c -> 1coke
                if (j >= 1 && n >= 2 && C[n-1][i][j-1] - C[n-2][i][j-1] == 8)
                    mc = min(mc, C[n-1][i][j-1]);
                
                // End of loop
                if (n == N && i == n5 && j == n10)
                    return mc;
                
                // DP!
                C[n][i][j] = mc;
            }
        }
    }
    return C[N][n5][n10];
}

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int q, b, n1, n5, n10;
    cin >> q;
    while (q--) {
        cin >> b >> n1 >> n5 >> n10;
        cout << dp(b, n5, n10, n1 + 5*n5 + 10*n10) << '\n';
    }

    return 0;
}