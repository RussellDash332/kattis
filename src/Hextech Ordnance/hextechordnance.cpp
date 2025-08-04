#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int BUF = 1<<15;
char inbuf[BUF]; int inpos, inlen;
char next() {
    if (inpos==inlen) {
        inpos=0; inlen=(int)fread(inbuf,1,BUF,stdin);
        //if (!inlen) return EOF;
    }
    return inbuf[inpos++];
}
ll read() {
    char c;
    while (!isdigit(c=next())) {}
    int x=c-48;
    while (isdigit(c=next())) x = x*10+(c-48);
    return x;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll N = read(), S = 0;
    vector<ll> A(N);
    for (int i = 0; i < N; ++i) { A[i] = read(); }
    priority_queue<tuple<ll, ll, ll>, vector<tuple<ll, ll, ll>>, greater<tuple<ll, ll, ll>>> Q;
    unordered_set<int> V;
    for (int i = 0; i < N-1; ++i) {
        ll a = min(A[i], A[i+1]), b = max(A[i], A[i+1]);
        if (b-a <= N) {
            V.insert(i*N+i+1);
            Q.push(make_tuple(b-a, i*N+i+1, a));
        }
    }
    while (!Q.empty() && S++ < N) {
        auto [d, ij, a] = Q.top();
        Q.pop();
        if (d > S) {
            cout << "unstable";
            return 0;
        }
        if (ij > N && V.find(ij-N) == V.end()) {
            V.insert(ij-N);
            ll a2 = min(a, A[ij/N-1]), b2 = max(d+a, A[ij/N-1]);
            Q.push(make_tuple(b2-a2, ij-N, a2));
        }
        if (ij%N < N-1 && V.find(ij+1) == V.end()) {
            V.insert(ij+1);
            ll a2 = min(a, A[ij%N+1]), b2 = max(d+a, A[ij%N+1]);
            Q.push(make_tuple(b2-a2, ij+1, a2));
        }
    }
    cout << (S < N ? "unstable" : "stable");
    return 0;
}