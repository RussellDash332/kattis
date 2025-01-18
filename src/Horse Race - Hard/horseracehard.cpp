#include <bits/stdc++.h>
#define FOR(i, n) for(int i = 0; i < n; ++i)
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
void write(int x) {
    int len = 0;
    for (; x>9; x/=10) nbuf[len++] = (char)(48+(x%10));
    wchar((char)(48+x));
    while (len) wchar(nbuf[--len]);
    wchar('\n');
}

// brute force works lol
int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    assert(atexit(flush_out)==0);
    int N = read(), A[N], B[2*N];
    vector<int> C;
    FOR(i, N) A[i] = read();
    FOR(i, N) B[i] = B[i+N] = read();
    FOR(i, N) {
        int c = 0;
        FOR(j, N) c += A[j] > B[i+j];
        if (2*c > N) C.push_back(i);
    }
    write(C.size());
    for (int i : C) write(i);
    return 0;
}