// Using std::complex

#include <bits/stdc++.h>
using namespace std;

vector<complex<double>> fft(vector<complex<double>> coef, bool inverse) { // n is guaranteed a power of 2
    int n = coef.size();
    
    if (n == 1)
        return coef;

    complex<double> z(0,0);
    vector<complex<double>> pe(n/2,z), po(n/2,z);
    for (int i = 0; i < n/2; i++) {
        pe[i] = coef[2*i];
        po[i] = coef[2*i+1];
    }

    vector<complex<double>> ye = fft(pe, inverse), yo = fft(po, inverse), y(n,z); // Recursion
    double angle = (inverse ? -2 : 2)*M_PI/n;
    complex<double> w(cos(angle), sin(angle)), wj = 1;

    for (int j = 0; j < n/2; j++) {
        y[j] = ye[j] + wj*yo[j];
        y[j+n/2] = ye[j] - wj*yo[j];
        wj *= w;
    }

    return y;
}

vector<int> multiply(vector<complex<double>> p1, vector<complex<double>> p2) {
    int n = p1.size(); // which is also p2.size()
    
    vector<complex<double>> fft1 = fft(p1, false), fft2 = fft(p2, false), fftr;

    for (int i = 0; i < n; i++)
        fftr.push_back(fft1[i]*fft2[i]);

    vector<complex<double>> ifftr = fft(fftr, true);

    vector<int> result;
    for (int i = 0; i < n; i++)
        result.push_back(round(real(ifftr[i])/n));

    return result;
}

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int t, d1, d2;
    double c;

    cin >> t;

    while (t--) {
        cin >> d1;
        vector<complex<double>> c1, c2;

        for (int i = 0; i <= d1; i++) {
            cin >> c;
            c1.push_back((complex<double>) c);
        }

        cin >> d2;
        for (int i = 0; i <= d2; i++) {
            cin >> c;
            c2.push_back((complex<double>) c);
        }

        int n = (int) pow(2,ceil(log2(d1+d2+1))); // fill to the nearest power of 2
        for (int i = 0; i < n-d1-1; i++)
            c1.push_back(0);
        
        for (int i = 0; i < n-d2-1; i++)
            c2.push_back(0);

        cout << d1+d2 << endl;
        vector<int> result = multiply(c1,c2);
        for (int i = 0; i <= d1+d2; i++)
            cout << result[i] << " ";
        cout << endl;
    }
    return 0;
}