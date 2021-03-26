#include <bits/stdc++.h>
using namespace std;

double f(double a, double b, double x) {
    return M_PI*((sqrt(M_PI)*erf(sqrt(2)*x)*pow(a,2))/(2*sqrt(2))+0.5*pow(b*x,2));
}

double g(double x) {
    return sqrt(x)*exp(-pow(x,2));
}

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    double V, minVol = DBL_MAX, a, b, h, v;
    int N, minIdx = 0;
    cin >> V >> N;

    for (int i = 0; i < N; i++) {
        cin >> a >> b >> h;
        // Non-Riemann sum goes in first
        v = f(a,b,h)-f(a,b,0);

        // Find Riemann sum of the gamma integral first
        int BREAKS = 90000;
        for (int i = 0; i < BREAKS-1; i++)
            v += a*b*h*M_PI/BREAKS*(g(h*i/BREAKS)+g(h*(i+1)/BREAKS)); // trapezoid rule

        if (abs(V-v) < minVol) {
            minVol = abs(V-v);
            minIdx = i;
        }
    }

    cout << minIdx;

    return 0;
}