#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vll = vector<ll>;
using hm = map<ll, int>;

const int BUF = 1<<15;

char inbuf[BUF]; int inpos, inlen;
char next() {
    if (inpos==inlen) {
        inpos=0; inlen=(int)fread(inbuf,1,BUF,stdin);
        if (!inlen) return EOF;
    }
    return inbuf[inpos++];
}
ll read() {
    char c;
    while (!isdigit(c=next())) {}
    ll x=c-48;
    while (isdigit(c=next())) x = x*10+(c-48);
    return x;
}

char outbuf[BUF], nbuf[20]; int outpos;
void flush_out() {
    fwrite(outbuf, 1, outpos, stdout); outpos = 0;
}
void wchar(char c) {
    if (outpos==BUF) flush_out();
    outbuf[outpos++] = c;
}
void write(int x) {
    int len = 0;
    for (; x>9; x/=10) nbuf[len++] = (char)(48+(x%10));
    wchar((char)(48+x));
    while (len) wchar(nbuf[--len]);
    wchar('\n');
}

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    assert(atexit(flush_out)==0);
    ll N=read(), Q=read(), M=0, C=N+3;
    vll P, H(N, 0), V;
    priority_queue<ll> S;
    hm Z;
    for (ll i = 0; i < N; i++) {
        ll k = read();
        while (k--) P.push_back(-read()*C+i);
    }
    while (Q--) {
        ll x=read();
        P.push_back(-x*C+N);
        V.push_back(x);
    }
    sort(P.begin(), P.end());
    for (ll c : P) {
        ll x = c/C, k = c%C;
        if (k < 0) { k += C; x -= 1; }
        if (k == N) {
            if (!S.empty()) Z[-x] = S.top()+1;
            else Z[-x] = N;
        } else {
            H[k]++;
            if (M < H[k]) {
                M = H[k];
                while (!S.empty()) S.pop();
            }
            if (M == H[k]) S.push(k);
        }
    }
    for (ll v : V) write(Z[v]);
    return 0;
}