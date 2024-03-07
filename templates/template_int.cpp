#include <bits/stdc++.h>
#define INF INT_MAX
#define pb push_back
#define ub upper_bound
#define lb lower_bound
#define FOR(n) for(int i = 0; i < n; ++i)
#define FOR(i, n) for(int i = 0; i < n; ++i)
#define FOR(i, a, b, s) for(int i = a; i < b; i += s)
#define FOR2(i, v) for(auto i : v)
#pragma GCC optimize("Ofast,unroll-loops")
#pragma GCC target("avx,avx2,fma")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,bmi,bmi2,lzcnt")
using namespace std;
using ll = long long;
using vi = vector<int>;
using vl = vector<long>;
using vll = vector<long long>;
using vvi = vector<vector<int>>;
using vvl = vector<vector<long>>;
using vvll = vector<vector<long long>>;
using mii = map<int, int>;
using pii = pair<int, int>;

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
    int sgn=1; char c;
    while (!isdigit(c=next())) if (c==45) sgn *= -1;
    int x=c-48;
    while (isdigit(c=next())) x = x*10+(c-48);
    return x*sgn;
}
int read_positive() {
    char c;
    while (!isdigit(c=next())) {}
    int x=c-48;
    while (isdigit(c=next())) x = x*10+(c-48);
    return x;
}
int read_one_digit() {
    char ch;
    while (!isdigit(ch=next())) {}
    return ch-48;
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
    if (x<0) { wchar('-'); x *= -1; }
    int len = 0;
    for (; x>9; x/=10) nbuf[len++] = (char)(48+(x%10));
    wchar((char)(48+x));
    while (len) wchar(nbuf[--len]);
    wchar('\n');
}
void write_positive(int x) {
    int len = 0;
    for (; x>9; x/=10) nbuf[len++] = (char)(48+(x%10));
    wchar((char)(48+x));
    while (len) wchar(nbuf[--len]);
    wchar('\n');
}
void write_one_digit(int x) {
    wchar((char)(48+x)); wchar('\n');
}

// 23 -34567 12332 9
int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    assert(atexit(flush_out)==0);
    int q = read();
    printf("A string.\n");
    write(q);
    write(read());
    write_positive(read_positive());
    write_one_digit(read_one_digit());
    return 0;
}