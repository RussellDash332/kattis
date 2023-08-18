#include <bits/stdc++.h>
using namespace std;
const double PI = atan(1.0)*4;

vector<complex<double>> fft(vector<complex<double>> &coef, bool inverse) {
    int n = coef.size();
    if (n == 1) return coef;
    complex<double> z(0,0);
    vector<complex<double>> pe(n/2,z), po(n/2,z);
    for (int i = 0; i < n/2; i++) {
        pe[i] = coef[2*i];
        po[i] = coef[2*i+1];
    }
    vector<complex<double>> ye = fft(pe, inverse), yo = fft(po, inverse), y(n,z);
    double angle = (inverse ? -2 : 2)*PI/n;
    complex<double> w(cos(angle), sin(angle)), wj = 1;
    for (int j = 0; j < n/2; j++) {
        y[j] = ye[j] + wj*yo[j];
        y[j+n/2] = ye[j] - wj*yo[j];
        wj *= w;
    }
    return y;
}

vector<int> multiply(vector<complex<double>> &p1, vector<complex<double>> &p2) {
    int n = p1.size();
    vector<complex<double>> fft1 = fft(p1, false), fft2 = fft(p2, false), fftr;
    for (int i = 0; i < n; i++) fftr.push_back(fft1[i]*fft2[i]);
    vector<complex<double>> ifftr = fft(fftr, true);
    vector<int> result;
    for (int i = 0; i < n; i++) result.push_back(round(real(ifftr[i])/n));
    return result;
}

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    cout.tie(NULL);
    int n;
    cin >> n;
    int m = (int) pow(2, ceil(log2(2*n-1)));
    vector<complex<double>> A(m);
    for (long long i = 1; i < n; i++) A[i*i%n] += 1;
    vector<int> B(n), C(n), result = multiply(A, A);
    long long ans = 0;
    for (int i = 0; i < m; i++) B[i%n] += result[i];
    for (int i = 0; i < n; i++) {
        B[2*i%n] -= real(A[i]);
        C[2*i%n] += real(A[i]);
    }
    for (int i = 0; i < n; i++) ans += real(A[i])*(B[i]/2+C[i]);
    cout << ans;
    return 0;
}