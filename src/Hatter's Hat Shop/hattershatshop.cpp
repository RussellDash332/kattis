#include <bits/stdc++.h>
#pragma GCC optimize("Ofast,unroll-loops")
#pragma GCC target("avx,avx2,fma")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,bmi,bmi2,lzcnt")
using namespace std;

const int BUF = 1<<15;

char inbuf[BUF]; int inpos, inlen;
char next() {
    if (inpos==inlen) {
        inpos=0; inlen=(int)fread(inbuf,1,BUF,stdin);
        //if (!inlen) return EOF;
    }
    return inbuf[inpos++];
}
int read() {
    char c;
    while (!isdigit(c=next())) {}
    int x=c-48;
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
void write(long long x) {
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
    int N = read(), M = read(), K = read();
    vector<int> D(M), C(M); // increment and capacity
    vector<vector<int>> P(M); // available hats
    vector<vector<long long>> S(M, {0}); // prefix sum
    long long Z = 0;
    priority_queue<pair<long long, int>> Q;
    vector<int> A(M, 0); // offset
    for (int i = 0; i < M; ++i) {
        D[i] = read(); C[i] = read();
    }
    for (int i = 0; i < N; ++i) {
        int t = read(), s = read();
        Z += s;
        P[--t].push_back(C[t]-s);
    }
    for (int i = 0; i < M; ++i) {
        sort(P[i].rbegin(), P[i].rend());
        for (int j : P[i]) S[i].push_back(S[i].back()+j);
    }
    for (int i = 0; i < M; ++i) {
        long long dz = 0;
        for (int x : P[i]) dz += min(x, D[i]);
        Q.emplace(dz, i);
    }
    while (K > 0 && !Q.empty()) {
        // try to devise hat idx
        auto [dz, idx] = Q.top();
        Q.pop();
        if (dz == 0) break;
        // how many times can we upgrade
        int u = max(min((P[idx].back()-A[idx])/D[idx], K), 1);
        while (!P[idx].empty() && P[idx].back()-A[idx] <= D[idx]*u) P[idx].pop_back();
        A[idx] += D[idx]*u; K -= u; Z += dz*u;
        auto p = lower_bound(P[idx].begin(), P[idx].end(), D[idx]+A[idx], greater<int>())-P[idx].begin();
        // -sum(min(P[idx][i]-A[idx], D[idx]) for i in range(len(P[idx])))
        // -sum(min(P[idx][i], A[idx]+D[idx])-A[idx] for i in range(len(P[idx])))
        // -sum(min(P[idx][i], A[idx]+D[idx]) for i in range(len(P[idx]))) + A[idx]*len(P[idx])
        // -((A[idx]+D[idx])*p + {P[idx][p] + P[idx][p+1] + ... + P[idx][len(P[idx])-1])} + A[idx]*len(P[idx])
        // -((A[idx]+D[idx])*p + {S[idx][len(P[idx])]-S[idx][p]}) + A[idx]*len(P[idx])
        Q.emplace((A[idx]+D[idx])*p + S[idx][P[idx].size()]-S[idx][p] - A[idx]*P[idx].size(), idx);
    }
    write(Z);
    return 0;
}