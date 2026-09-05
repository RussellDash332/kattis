#include <bits/stdc++.h>
#define eb emplace_back
#define ub upper_bound
#pragma GCC optimize("Ofast,unroll-loops")
#pragma GCC target("avx,avx2,fma")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,bmi,bmi2,lzcnt")
using namespace std;
using ll = long;
using vll = vector<ll>;
using vvll = vector<vll>;

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

char outbuf[BUF], nbuf[11]; int outpos;
void flush_out() {
    fwrite(outbuf, 1, outpos, stdout); outpos = 0;
}
void wchar(char c) {
    if (outpos==BUF) flush_out();
    outbuf[outpos++] = c;
}
void write(ll x) {
    int len = 0;
    for (; x>9; x/=10) nbuf[len++] = (char)(48+(x%10));
    wchar((char)(48+x));
    while (len) wchar(nbuf[--len]);
}

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    assert(atexit(flush_out)==0);
    int N = read();
    vll W(N);
    for (int i = 0; i < N; i++) W[i] = read();
    int K = ceil(sqrt(N));
    vvll Z, Y;
    bool flip = false;
    for (vvll* A : {&Z, &Y}) {
        vll tmp = W;
        if (flip) reverse(tmp.begin(), tmp.end());
        flip ^= 1;
        for (int _ = 0; _ < K; _++) {
            if (tmp.empty()) break;
            vll b, S;
            for (ll i : tmp) {
                auto p = ub(b.begin(), b.end(), i);
                if (p == b.end()) b.eb(i);
                else { S.eb(*p); *p = i; }
            }
            A->eb(move(b)); tmp = move(S);
        }
    }
    Z.resize(Y[0].size());
    for (const auto& y : Y)
        for (int i = K; i < y.size(); i++) Z[i].eb(y[i]);
    for (const auto& b : Z) {
        for (int i = 0; i < b.size(); i++) {
            if (i) wchar(' ');
            write(b[i]);
        }
        wchar(';'); wchar('\n');
    }
    return 0;
}